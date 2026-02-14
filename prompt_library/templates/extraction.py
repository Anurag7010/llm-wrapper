from prompt_library.models import PromptTemplate
from prompt_library.registry import registry

extraction_v1 = PromptTemplate(
    name          = "extraction",
    version       = "v1",
    description   = "Extracts specific structured fields from unstructured text",
    required_vars = ["text", "fields"],
    template      = """You are a precise structured data extraction assistant.

ROLE:
Your job is to extract specific fields from the provided text.
You are not a summarizer — you extract only what is explicitly asked for.
You do not use outside knowledge, opinions, or assumptions.

TEXT:
{text}

FIELDS TO EXTRACT:
{fields}

OUTPUT RULES:
- Extract each requested field and output exactly one line per field
- Use this exact format for every line:  field_name: value
- Output fields in the exact order they were listed above
- If a field is not found in the text, output:  field_name: NOT FOUND
- Do not include explanations, headers, or any other text in your response
- Do not wrap output in code blocks or quotes

KNOWLEDGE BOUNDARY:
Only extract information explicitly present in the TEXT above.
Never infer, assume, or supplement with external knowledge."""
)

registry.register(extraction_v1)
