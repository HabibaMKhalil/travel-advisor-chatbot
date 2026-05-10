import os
import json

INPUT_DIR = "../data/chunks"
OUTPUT_FILE = "../data/final_chunks.json"


def load_chunks(subfolder):
    folder = os.path.join(INPUT_DIR, subfolder)
    records = []

    for filename in os.listdir(folder):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        for chunk in chunks:
            record = {
                "id": f"{subfolder}_{filename.replace('.json','')}_{chunk['chunk_id']}",
                "text": chunk["text"],
                "metadata": {
                    "destination": chunk.get("destination"),
                    "content_type": chunk.get("content_type"),
                    "parent_title": chunk.get("parent_title"),
                    "source_url": chunk.get("source_url"),
                    "chunk_id": chunk.get("chunk_id")
                }
            }
            records.append(record)

    return records


def main():
    print("[INFO] Preparing final chunk dataset...")

    all_records = []
    for sub in ["tips", "destinations"]:
        all_records.extend(load_chunks(sub))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_records, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Total chunks ready for embedding: {len(all_records)}")
    print(f"[INFO] Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
