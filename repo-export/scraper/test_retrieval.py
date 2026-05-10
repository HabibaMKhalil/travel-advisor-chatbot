import chromadb

DB_DIR = r"C:\NGU\Semester 7\NLP\Project\Phase 1\travel-advisor-chatbot\vector_db\chroma"
COLLECTION_NAME = "travel_advisor"


def main():
    client = chromadb.PersistentClient(path=DB_DIR)

    collections = client.list_collections()
    print("[INFO] Collections:", [c.name for c in collections])

    if not collections:
        print("[ERROR] No collections found — DB not loaded correctly")
        return

    collection = client.get_collection(name=COLLECTION_NAME)

    query = "Is Paris safe for tourists?"
    print(f"\n[QUERY] {query}\n")

    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    if not results["documents"][0]:
        print("[WARN] No results returned")
        return

    for i, doc in enumerate(results["documents"][0]):
        print(f"--- Result {i + 1} ---")
        print(doc[:300])
        print()


if __name__ == "__main__":
    main()
