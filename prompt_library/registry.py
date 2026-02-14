from prompt_library.models import PromptTemplate

class TemplateRegistry:

    def __init__(self):
        self.temp_dict = {} #instance var

    def register(self, template: PromptTemplate) -> None:
        key = f"{template.name}:{template.version}"
        self.temp_dict[key] = template

    def get(self, name: str, version: str) -> PromptTemplate:
        key = f"{name}:{version}"
        if key not in self.temp_dict:
            raise ValueError(
                f"Template '{name}' version '{version}' not found in registry"
            )
        return self.temp_dict[key]
    def list_templates(self) -> list:
        return list(self.temp_dict.keys())

# Single shared instance 
registry = TemplateRegistry()