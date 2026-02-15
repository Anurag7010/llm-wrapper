import json
def build_schema_string(schema: dict) -> str:
    lines = "{\n"
    for key, value in schema.items():
        lines += f'    "{key}": <{value}>,\n'
    lines = lines.rstrip(",\n")  
    lines += "\n}"
    return lines

TYPE_MAP = {
    "string": str,
    "integer": int,
    "boolean": bool,
    "float": float
}

def validate_output(raw: str, schema: dict) -> dict:
    start=raw.find("{")
    end=raw.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("Output does not contain a valid JSON object")
    json_str = raw[start:end+1]
    try:
        parsed=json.loads(json_str) # Note: JSON null becomes Python None automatically
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON parsing failed: {e}. Raw output: {json_str[:100]}")
    
    missing_keys= set(schema)-set(parsed)
    if missing_keys:
        raise ValueError(f"Missing keys in output: {missing_keys}")
    
    for field, expected_type_str in schema.items():
        value = parsed[field]
        expected_type = TYPE_MAP.get(expected_type_str)
        if expected_type is None:
            raise ValueError(f"Unknown expected type '{expected_type_str}' for field '{field}'")
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(f"Field '{field}' is expected to be of type '{expected_type_str}' but got '{type(value).__name__}'")
    return parsed
        
        
        
    
            