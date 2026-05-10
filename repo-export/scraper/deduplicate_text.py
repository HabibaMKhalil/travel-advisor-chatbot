import os
import json
import hashlib

INPUT_DIR = "../data/processed_text"
OUTPUT_DIR = "../data/deduplicated_text"


def hash_text(text: str) -> str:
    """
    Generate a hash for text content.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def process_folder(subfolder):
    input_folder = os.path.join(INPUT_DIR, subfolder)
    output_folder = os.path.join(OUTPUT_DIR, subfolder)

    os.makedirs(output_folder, exist_ok=True)

    seen_hashes = set()
    kept = 0
    removed = 0

    for filename in os.listdir(input_folder):
        if not filename.endswith(".json"):
            continue

        in_path = os.path.join(input_folder, filename)

        with open(in_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        content = data.get("content", "").strip()
        content_hash = hash_text(content)

        if content_hash in seen_hashes:
            removed += 1
            continue

        seen_hashes.add(content_hash)

        out_path = os.path.join(output_folder, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        kept += 1

    print(f"[{subfolder.upper()}] Kept: {kept}, Removed duplicates: {removed}")


def main():
    print("[INFO] Starting deduplication...")

    for sub in ["tips", "destinations"]:
        process_folder(sub)

    print("[INFO] Deduplication completed.")


if __name__ == "__main__":
    main()
