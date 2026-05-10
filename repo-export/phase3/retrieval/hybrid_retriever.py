import chromadb

DB_DIR = r"C:\NGU\Semester 7\NLP\Project\Travel-advisor-chatbot\vector_db\chroma"

AUTHORITATIVE_COLLECTION = "authoritative_travel"
GENERAL_COLLECTION = "travel_advisor"


class HybridRetriever:
    def retrieve(self, query):
        auth_results = self.auth_col.query(
            query_texts=[query],
            n_results=self.top_k
        )

        if auth_results["documents"] and auth_results["documents"][0]:
            return (
                auth_results["documents"][0],
                auth_results["metadatas"][0],
                "authoritative"
            )

        general_results = self.general_col.query(
            query_texts=[query],
            n_results=self.top_k
        )

        if general_results["documents"] and general_results["documents"][0]:
            return (
                general_results["documents"][0],
                general_results["metadatas"][0],
                "general"
            )

        return [], [], "none"
