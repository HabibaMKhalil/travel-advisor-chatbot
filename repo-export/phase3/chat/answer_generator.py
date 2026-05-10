from phase3.prompts.prompts import SYSTEM_PROMPT, ANSWER_PROMPT_TEMPLATE

def generate_answer(question, docs, metas):
    if not docs:
        return (
            "I don’t have enough reliable information to answer this question safely.",
            []
        )

    context_blocks = []
    citations = []

    for doc, meta in zip(docs, metas):
        context_blocks.append(doc)
        citations.append(f"{meta.get('source')} – {meta.get('destination')}")

    context = "\n\n".join(context_blocks)

    prompt = ANSWER_PROMPT_TEMPLATE.format(
        question=question,
        context=context
    )

    answer = context_blocks[0]

    return answer, citations
