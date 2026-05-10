from phase3.retrieval.hybrid_retriever import HybridRetriever
from phase3.chat.answer_generator import generate_answer

def chat():
    retriever = HybridRetriever(top_k=3)

    while True:
        question = input("\nAsk a travel question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        docs, metas, source_type = retriever.retrieve(question)

        answer, citations = generate_answer(question, docs, metas)

        print("\n--- ANSWER ---")
        print(answer)

        if citations:
            print("\nSources:")
            for c in set(citations):
                print(f"- {c}")

        if source_type == "none":
            print("\n[Note] No relevant documents were found.")


if __name__ == "__main__":
    chat()
