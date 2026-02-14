from llm_client import generate_response
from prompt_library import build_prompt
from prompt_library.registry import registry


def run_qa():
    question = input("Enter your question: ")
    context  = input("Enter context: ")

    prompt = build_prompt(
        template_name = "qa_assistant",
        variables     = {
            "question": question,
            "context":  context
        }
    )
    return prompt

def run_summarization():
    article_text  = input("Paste article text: ")
    language      = input("Output language (e.g. English): ")
    max_sentences = input("Max sentences in summary: ")

    prompt = build_prompt(
        template_name = "summarization",
        variables     = {
            "article_text":  article_text,
            "language":      language,
            "max_sentences": max_sentences
        }
    )
    return prompt


def run_extraction():
    text   = input("Paste text to extract from: ")
    fields = input("Fields to extract (e.g. name, date, location): ")

    prompt = build_prompt(
        template_name = "extraction",
        variables     = {
            "text":   text,
            "fields": fields
        }
    )
    return prompt


if __name__ == "__main__":

    print("\nAvailable templates:")
    for t in registry.list_templates():
        print(f"  - {t}")

    print("\nSelect task:")
    print("  1. QA Assistant")
    print("  2. Summarization")
    print("  3. Extraction")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        prompt = run_qa()
    elif choice == "2":
        prompt = run_summarization()
    elif choice == "3":
        prompt = run_extraction()
    else:
        print("Invalid choice")
        exit(1)

    # existing flow — unchanged
    result = generate_response(prompt)

    if result["success"]:
        print(f"\nResponse: {result['response']}")
        print(f"\nMetadata:")
        print(f"  Latency:       {result['latency']:.2f}s")
        print(f"  Retries:       {result['retries']}")
        print(f"  Prompt length: {result['prompt_length']} chars")
    else:
        print("\n✗ Request Failed")
        print(f"  Error:             {result.get('error', 'Unknown error')}")
        print(f"  Retries attempted: {result['retries']}")