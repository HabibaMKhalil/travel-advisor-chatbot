import requests
import time
import json
import os
import re
from bs4 import BeautifulSoup
from config import DESTINATION_BASE_URLS, HEADERS, REQUEST_DELAY

RAW_DIR = "../data/raw_html/destinations"
CLEAN_DIR = "../data/cleaned_text/destinations"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)

def clean_text(text):
    """
    Basic text cleaning:
    - Remove reference markers like [1], [2]
    - Normalize the whitespace
    """
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def scrape_page(url):
    """
    Fetch HTML content of a page.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def parse_content(html):
    """
    Parse title and main textual content from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown"

    content_blocks = []
    for tag in soup.find_all(["h2", "h3", "p", "li"]):
        text = tag.get_text(strip=True)
        if len(text) > 30:
            content_blocks.append(clean_text(text))

    return title, "\n".join(content_blocks)


def main():
    success = 0
    failed = 0

    print(f"[INFO] Starting destination scraping ({len(DESTINATION_BASE_URLS)} pages)")

    for url in DESTINATION_BASE_URLS:
        print(f"[INFO] Scraping {url}")

        html = scrape_page(url)
        if not html:
            failed += 1
            continue

        filename = url.split("/")[-1]

        with open(f"{RAW_DIR}/{filename}.html", "w", encoding="utf-8") as f:
            f.write(html)

        title, content = parse_content(html)

        data = {
            "title": title,
            "destination": title,
            "content": content,
            "source_url": url,
            "content_type": "destination"
        }

        with open(f"{CLEAN_DIR}/{filename}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        success += 1
        time.sleep(REQUEST_DELAY)

    print(f"[SUMMARY] Success: {success}, Failed: {failed}, Total: {len(DESTINATION_BASE_URLS)}")


if __name__ == "__main__":
    main()
