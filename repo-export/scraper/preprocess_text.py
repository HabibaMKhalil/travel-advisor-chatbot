import os
import json
import re

INPUT_DIR = "../data/cleaned_text"
OUTPUT_DIR = "../data/processed_text"

MIN_CONTENT_LENGTH = 200  # characters


def normalize_text(text: str) -> str:
    """
    Normalize text for NLP processing.
    """
    if not text:
        return ""

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove stray symbols
    text = re.sub(r"[•◆►]", "", text)

    return text.strip()


def process_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    content = data.get("content", "")
    normalized = normalize_text(content)

    if len(normalized) < MIN_CONTENT_LENGTH:
        return False  # skip noisy/short docs

    data["content"] = normalized

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return True


def process_folder(subfolder):
    input_folder = os.path.join(INPUT_DIR, subfolder)
    output_folder = os.path.join(OUTPUT_DIR, subfolder)

    os.makedirs(output_folder, exist_ok=True)

    kept = 0
    skipped = 0

    for filename in os.listdir(input_folder):
        if not filename.endswith(".json"):
            continue

        in_path = os.path.join(input_folder, filename)
        out_path = os.path.join(output_folder, filename)

        if process_file(in_path, out_path):
            kept += 1
        else:
            skipped += 1

    print(f"[{subfolder.upper()}] Kept: {kept}, Skipped: {skipped}")


def main():
    print("[INFO] Starting text normalization...")

    for sub in ["tips", "destinations"]:
        process_folder(sub)

    print("[INFO] Text preprocessing completed.")


if __name__ == "__main__":
    main()
