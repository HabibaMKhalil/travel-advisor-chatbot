import requests
import time
import json
import os
import re
from bs4 import BeautifulSoup
from config import TRAVEL_TIPS_URLS, HEADERS, REQUEST_DELAY

RAW_DIR = "../data/raw_html/tips"
CLEAN_DIR = "../data/cleaned_text/tips"

# Making sure urls are safely loaded
print("Loaded TRAVEL_TIPS_URLS:", TRAVEL_TIPS_URLS)

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)


def clean_text(text):
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def scrape_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def main():
    for url in TRAVEL_TIPS_URLS:
        print(f"[INFO] Scraping {url}")
        html = scrape_page(url)
        if not html:
            continue

        filename = url.split("/")[-1]

        with open(f"{RAW_DIR}/{filename}.html", "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1").get_text(strip=True)

        content_blocks = []
        for tag in soup.find_all(["h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if len(text) > 30:
                content_blocks.append(clean_text(text))

        data = {
            "title": title,
            "destination": None,
            "content": "\n".join(content_blocks),
            "source_url": url,
            "content_type": "travel_tips"
        }

        with open(f"{CLEAN_DIR}/{filename}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
