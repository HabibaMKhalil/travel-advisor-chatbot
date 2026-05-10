import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import HEADERS, MAX_DESTINATIONS

BASE = "https://en.wikivoyage.org"

DESTINATIONS_INDEX = "https://en.wikivoyage.org/wiki/Destinations"

def is_valid_destination(href: str) -> bool:
    if not href or not href.startswith("/wiki/"):
        return False

    if ":" in href:
        return False

    if href in [
        "/wiki/Main_Page",
        "/wiki/Destinations",
        "/wiki/Star_articles"
    ]:
        return False

    if "#" in href or "?action=" in href:
        return False

    return True

def discover():
    discovered = []
    seen = set()

    r = requests.get(DESTINATIONS_INDEX, headers=HEADERS, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.select("a[href]"):
        href = a.get("href")

        if is_valid_destination(href):
            full_url = urljoin(BASE, href)

            if full_url not in seen:
                seen.add(full_url)
                discovered.append(full_url)

        if len(discovered) >= MAX_DESTINATIONS:
            break

    return discovered

if __name__ == "__main__":
    urls = discover()
    print(f"[INFO] Discovered {len(urls)} destinations")
    for u in urls[:20]:
        print(" -", u)
