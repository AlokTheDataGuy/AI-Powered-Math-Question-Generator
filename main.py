# main.py
from __future__ import annotations

import argparse

from llm_clients import HFClient, OllamaClient, BaseLLMClient
from llm_generator import AIQuestionGenerator, TxtExporter, WordExporter


def main() -> None:
    parser = argparse.ArgumentParser(description="LLM-oriented Math Question Generator (free local models)")
    parser.add_argument("--num", type=int, default=2, help="Number of questions")
    parser.add_argument("--llm", choices=["hf", "ollama", "none"], default="ollama", help="LLM backend")
    parser.add_argument("--hf_model", type=str, default="mistralai/Mistral-7B-Instruct-v0.2", help="HF model name")
    parser.add_argument("--ollama_model", type=str, default="mistral:7b", help="Ollama model name")
    parser.add_argument("--title", type=str, default="AI-Generated Quantitative Math Assessment",
                        help="Assessment title")
    args = parser.parse_args()

    # Initialize client
    client: BaseLLMClient | None
    if args.llm == "hf":
        client = HFClient(model=args.hf_model)
    elif args.llm == "ollama":
        client = OllamaClient(model=args.ollama_model)
    else:
        client = None

    print("🚀 Generating Math Assessment Questions...")
    gen = AIQuestionGenerator(llm_client=client)

    questions = gen.generate_assessment(args.num)

    # TXT output (HR-required tag format)
    txt_path = TxtExporter().export(questions, filename="assessment_questions.txt", title=args.title)

    # DOCX output with images (generated and embedded automatically)
    doc = WordExporter(filename="math_assessment.docx")
    doc.add_title()
    for i, q in enumerate(questions, 1):
        img_path = None
        if q.get("has_image") and "points_data" in q:
            img_path = gen.create_graph_image(q, f"question_{i}_graph.png")
        doc.add_question(q, i, image_path=img_path)
    doc_path = doc.save()

    print("✅ Assessment generation completed!")
    print(f"📝 Formatted questions: {txt_path}")
    print(f"📄 Word document: {doc_path}")


if __name__ == "__main__":
    main()
