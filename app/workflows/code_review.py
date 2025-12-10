def extract_functions(state):
    code = state["code"]
    state["functions"] = code.count("def ")
    return state


def check_complexity(state):
    f = state["functions"]
    state["complexity"] = f * 3
    return state


def detect_issues(state):
    complexity = state["complexity"]
    state["issues"] = complexity // 2
    return state


def suggest_improvements(state):
    issues = state["issues"]
    improvements = []

    if issues > 3:
        improvements.append("Reduce nested loops")
    if issues > 5:
        improvements.append("Break down long functions")

    state["improvements"] = improvements
    state["quality_score"] = max(1, 10 - issues)
    return state


from app.engine.registry import tool_registry

def apply_tool(state):
    tool = tool_registry.get("double")
    result = tool(5)   # test input
    state["tool_output"] = result
    return state
