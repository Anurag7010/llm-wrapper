from prompt_library.registry import registry


def build_prompt(
    template_name: str,
    variables: dict,
    version: str = "v1"
) -> str:
    # STAGE 1 — retrieve template
    template = registry.get(template_name, version)

    # STAGE 2 — validate required variables
    required = set(template.required_vars)
    provided = set(variables.keys())
    missing = required - provided

    if missing:
        raise ValueError(
            f"Missing required variables for template "
            f"'{template_name}:{version}': {missing}"
        )

    # STAGE 3 — inject variables
    prompt = template.template.format_map(variables)

    # STAGE 4 — return final prompt string
    return prompt
