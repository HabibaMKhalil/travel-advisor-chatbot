import chromadb

DB_DIR = r"C:\NGU\Semester 7\NLP\Project\Phase 1\travel-advisor-chatbot\vector_db\chroma"
COLLECTION_NAME = "authoritative_travel"

def main():
    client = chromadb.PersistentClient(path=DB_DIR)
    print("[INFO] Collections:", [c.name for c in client.list_collections()])

    col = client.get_collection(COLLECTION_NAME)

    query = "Is France safe for tourists?"
    res = col.query(query_texts=[query], n_results=3)

    print("\n[QUERY]", query)
    if not res["documents"][0]:
        print("[WARN] No results")
        return

    for i, doc in enumerate(res["documents"][0]):
        meta = res["metadatas"][0][i]
        print(f"\n--- Result {i+1} ---")
        print(doc)
        print("META:", meta)

if __name__ == "__main__":
    main()
