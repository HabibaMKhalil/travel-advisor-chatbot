import json
import os
import re
from pathlib import Path

MANIFEST_PATH = "authoritative_data/manifest.json"
OUTPUT_DIR = "phase3_processed"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "authoritative_cleaned.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    cleaned_docs = []

    for item in manifest:
        with open(item["path"], "r", encoding="utf-8") as f:
            doc = json.load(f)

        cleaned_docs.append({
            "destination": doc["destination"],
            "source": doc["source"],
            "content_type": doc["content_type"],
            "authority_level": doc["authority_level"],
            "retrieval_priority": doc.get("retrieval_priority", 1),
            "url": doc["url"],
            "content": clean_text(doc["content"])
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned_docs, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Cleaned authoritative data written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
