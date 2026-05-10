import os
import json

INPUT_DIR = "../data/deduplicated_text"
OUTPUT_DIR = "../data/chunks"

CHUNK_SIZE = 500      # characters
CHUNK_OVERLAP = 100   # characters


def chunk_text(text):
    """
    Split text into overlapping chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def process_folder(subfolder):
    input_folder = os.path.join(INPUT_DIR, subfolder)
    output_folder = os.path.join(OUTPUT_DIR, subfolder)

    os.makedirs(output_folder, exist_ok=True)

    total_chunks = 0

    for filename in os.listdir(input_folder):
        if not filename.endswith(".json"):
            continue

        in_path = os.path.join(input_folder, filename)

        with open(in_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        content = data.get("content", "")
        chunks = chunk_text(content)

        chunk_records = []
        for idx, chunk in enumerate(chunks):
            record = {
                "chunk_id": idx,
                "parent_title": data.get("title"),
                "destination": data.get("destination"),
                "content_type": data.get("content_type"),
                "source_url": data.get("source_url"),
                "text": chunk
            }
            chunk_records.append(record)

        out_path = os.path.join(output_folder, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk_records, f, ensure_ascii=False, indent=2)

        total_chunks += len(chunk_records)

    print(f"[{subfolder.upper()}] Total chunks created: {total_chunks}")


def main():
    print("[INFO] Starting text chunking...")

    for sub in ["tips", "destinations"]:
        process_folder(sub)

    print("[INFO] Chunking completed.")


if __name__ == "__main__":
    main()
