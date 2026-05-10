import json
import os
import chromadb

DATA_FILE = "phase3_processed/authoritative_chunks.json"
DB_DIR = r"C:\NGU\Semester 7\NLP\Project\Travel-advisor-chatbot\vector_db\chroma"
COLLECTION_NAME = "authoritative_travel"


def sanitize_metadata(metadata: dict) -> dict:
    clean = {}
    for k, v in metadata.items():
        if v is None:
            clean[k] = "unknown"
        elif isinstance(v, (str, int, float, bool)):
            clean[k] = v
        else:
            clean[k] = str(v)
    return clean


def main():
    print("[INFO] Loading authoritative chunks...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)

    texts = [r["text"] for r in records]
    metadatas = [sanitize_metadata(r["metadata"]) for r in records]
    ids = [r["id"] for r in records]

    print(f"[INFO] Chunks loaded: {len(texts)}")

    print("[INFO] Initializing Chroma PersistentClient...")
    client = chromadb.PersistentClient(path=DB_DIR)

    print("[INFO] Creating / loading authoritative collection...")
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    print("[INFO] Adding authoritative documents...")
    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

    print("[SUCCESS] Authoritative vector DB updated.")
    print(f"[SUCCESS] Collection: {COLLECTION_NAME}")
    print(f"[SUCCESS] DB path: {DB_DIR}")


if __name__ == "__main__":
    main()
