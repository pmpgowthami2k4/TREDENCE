# tool registry
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, fn):
        self.tools[name] = fn

    def get(self, name: str):
        return self.tools.get(name)


tool_registry = ToolRegistry()


def double(x):
    return {"result": x * 2}

def triple(x):
    return {"result": x * 3}

def square(x):
    return {"result": x * x}

# Register tools
tool_registry.register("double", double)
tool_registry.register("triple", triple)
tool_registry.register("square", square)
