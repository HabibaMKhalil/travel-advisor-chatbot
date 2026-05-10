import json
import os

INPUT_FILE = "phase3_processed/authoritative_cleaned.json"
OUTPUT_FILE = "phase3_processed/authoritative_chunks.json"

CHUNK_SIZE = 200
OVERLAP = 50


def chunk_text(text, size, overlap):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start += size - overlap

    return chunks


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        docs = json.load(f)

    all_chunks = []
    chunk_counter = 0

    for doc in docs:
        chunks = chunk_text(doc["content"], CHUNK_SIZE, OVERLAP)

        for chunk in chunks:
            all_chunks.append({
                "id": f"auth_chunk_{chunk_counter}",
                "text": chunk,
                "metadata": {
                    "destination": doc["destination"],
                    "source": doc["source"],
                    "content_type": doc["content_type"],
                    "authority_level": doc["authority_level"],
                    "retrieval_priority": doc["retrieval_priority"],
                    "url": doc["url"]
                }
            })
            chunk_counter += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Created {len(all_chunks)} authoritative chunks")


if __name__ == "__main__":
    main()
