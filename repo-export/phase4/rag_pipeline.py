import sys
import os
import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from phase3.retrieval.hybrid_retriever import HybridRetriever

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi:latest"  


class TravelAdvisorRAG:
    def __init__(self):
        self.retriever = HybridRetriever(top_k=3)

    def _call_llm(self, prompt: str) -> str:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        except Exception:
            return ""

        if response.status_code != 200:
            return ""

        return response.json().get("response", "").strip()

    def answer(self, question: str):
        docs, metas, source_type = self.retriever.retrieve(question)

        if not docs:
            return {
                "answer": "I don’t have enough reliable travel information to answer this question.",
                "sources": []
            }

        context = "\n\n".join(docs)

        prompt = f"""
You are a professional travel advisor.

You MUST answer the question using ONLY the information in the context.
Do NOT invent facts.
Do NOT mention documents or context explicitly.
Summarize clearly and helpfully.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = self._call_llm(prompt)

        if not answer:
            answer = "I cannot generate an answer based on the retrieved travel information."

        sources = []
        for m in metas:
            src = f"{m.get('source', 'Unknown Source')} – {m.get('destination', '').strip()}"
            if src not in sources:
                sources.append(src)

        return {
            "answer": answer,
            "sources": sources
        }
