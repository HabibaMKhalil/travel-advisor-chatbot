from phase4.rag_pipeline import TravelAdvisorRAG


def main():
    rag = TravelAdvisorRAG()

    print("Travel Advisor Chatbot (Local, Free LLM)")

    while True:
        question = input("\nAsk a travel question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        result = rag.answer(question)

        print("\nANSWER:")
        print(result["answer"])

        if result["sources"]:
            print("\nSources:")
            for s in result["sources"]:
                print("-", s)


if __name__ == "__main__":
    main()
