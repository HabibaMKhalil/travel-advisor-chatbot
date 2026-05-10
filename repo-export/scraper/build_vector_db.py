import json
import os
import chromadb

DATA_FILE = "../data/final_chunks.json"
DB_DIR = r"C:\NGU\Semester 7\NLP\Project\Phase 1\travel-advisor-chatbot\vector_db\chroma"
COLLECTION_NAME = "travel_advisor"

os.makedirs(DB_DIR, exist_ok=True)


def sanitize_metadata(metadata):
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
    print("[INFO] Loading chunks...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        records = json.load(f)

    texts = [r["text"] for r in records]
    metadatas = [sanitize_metadata(r["metadata"]) for r in records]
    ids = [r["id"] for r in records]

    print(f"[INFO] Chunks: {len(texts)}")
    
    client = chromadb.PersistentClient(path=DB_DIR)

    print("[INFO] Creating / loading collection...")
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    print("[INFO] Adding documents...")
    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

    print("[SUCCESS] Vector DB built at:", DB_DIR)


if __name__ == "__main__":
    main()
