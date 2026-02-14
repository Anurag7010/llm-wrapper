from dataclasses import dataclass
from typing import List


@dataclass
class PromptTemplate:
    name: str                    # unique identifier e.g. "qa_assistant"
    version: str                 # version tag  e.g. "v1", "v2"
    description: str             # human-readable explanation for developers
    required_vars: List[str]     # variables builder must validate before render
    template: str                # actual prompt string with {placeholders}

    def render(self, variables: dict) -> str:
        return self.template     # stub — full implementation in builder.py