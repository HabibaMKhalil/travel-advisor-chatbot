import subprocess


class LocalLLM:
    def __init__(self, model="phi"):
        self.model = model

    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"   
        )

        if result.returncode != 0:
            return "[ERROR] Local LLM failed to generate response."

        return result.stdout.strip()
import subprocess


class LocalLLM:
    def __init__(self, model="phi"):
        self.model = model

    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"  
        )

        if result.returncode != 0:
            return "[ERROR] Local LLM failed to generate response."

        return result.stdout.strip()
