from llm_client import generate_response
from prompt_library.templates.structured_output import STRUCTURED_PROMPT
from .validator import build_schema_string, validate_output
from logger import logger

MAX_VALIDATION_RETRIES = 3

def generate_structured(prompt: str, schema: dict) -> dict:
    final_prompt= STRUCTURED_PROMPT.format(task_description=prompt,schema_definition= build_schema_string(schema))
    
    for attempt in range(MAX_VALIDATION_RETRIES):

        result = generate_response(final_prompt)
        try:
            raw=result["response"]
            parsed = validate_output(raw,schema)
            
            return {
                "success": True,
                "data": parsed,
                "error": None,
                "retries": attempt,
                "latency": result["latency"]    
            }
        except ValueError as e:
            logger.warning(
                f"validation_failed "
                f"attempt={attempt + 1} "
                f"error={str(e)}"           
                f"raw={result['response'][:100]}"
            )    
    return {
        "success": False,
        "data": None,
        "error": "Validation failed after all retries",
        "retries": MAX_VALIDATION_RETRIES,
        "latency": None
    }    
