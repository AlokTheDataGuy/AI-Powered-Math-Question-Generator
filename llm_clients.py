# llm_clients.py
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class LLMResult:
    ok: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class BaseLLMClient:
    def generate(self, prompt: str, max_new_tokens: int = 768) -> LLMResult:
        raise NotImplementedError


def _extract_json_block(text: str) -> LLMResult:
    """
    Extract the first JSON object from the text and parse it.
    """
    try:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            payload = text[start : end + 1]
            data = json.loads(payload)
            return LLMResult(True, data=data)
        return LLMResult(False, error="No JSON object found in model output")
    except Exception as e:
        return LLMResult(False, error=f"JSON parse failed: {e}")


class HFClient(BaseLLMClient):
    """
    Hugging Face Transformers local pipeline client (free, local).
    """

    def __init__(self, model: str = "mistralai/Mistral-7B-Instruct-v0.2", **gen_kwargs: Any) -> None:
        self.model = model
        self.gen_kwargs = {"max_new_tokens": 700, "temperature": 0.5, "top_p": 0.9, **gen_kwargs}
        try:
            from transformers import pipeline  # type: ignore
            self._pipeline = pipeline(
                task="text-generation",
                model=self.model,
                tokenizer=self.model,
                device_map="auto",
            )
            self._ok = True
            self._import_error = None
        except Exception as e:
            self._pipeline = None
            self._ok = False
            self._import_error = str(e)

    def generate(self, prompt: str, max_new_tokens: int = 768) -> LLMResult:
        if not self._ok or self._pipeline is None:
            return LLMResult(False, error=f"Transformers pipeline not available: {self._import_error}")
        try:
            out = self._pipeline(prompt, **{**self.gen_kwargs, "max_new_tokens": max_new_tokens})
            text = out[0]["generated_text"]
            return _extract_json_block(text)
        except Exception as e:
            return LLMResult(False, error=str(e))


class OllamaClient(BaseLLMClient):
    """
    Ollama client via subprocess (free, local).
    """

    def __init__(self, model: str = "mistral:7b") -> None:
        self.model = model
        self._have_ollama = shutil.which("ollama") is not None

    def generate(self, prompt: str, max_new_tokens: int = 768) -> LLMResult:
        if not self._have_ollama:
            return LLMResult(False, error="ollama binary not found on PATH")
        try:
            import subprocess
            cmd = ["ollama", "run", self.model]
            proc = subprocess.run(cmd, input=prompt.encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode != 0:
                return LLMResult(False, error=proc.stderr.decode("utf-8", "ignore"))
            text = proc.stdout.decode("utf-8", "ignore")
            return _extract_json_block(text)
        except Exception as e:
            return LLMResult(False, error=str(e))
