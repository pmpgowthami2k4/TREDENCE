# from fastapi import FastAPI
# from pydantic import BaseModel
# from app.engine.graph import Graph
# from app.engine.runner import runner
# from app.workflows import code_review

# app = FastAPI()

# class CreateGraphRequest(BaseModel):
#     nodes: dict
#     edges: dict

# class RunRequest(BaseModel):
#     graph_id: str
#     state: dict

# @app.post("/graph/create")
# def create_graph(req: CreateGraphRequest):
#     graph = Graph()
#     for name in req.nodes:
#         fn = getattr(code_review, name)
#         graph.add_node(name, fn)
#     for src, dst in req.edges.items():
#         graph.add_edge(src, dst)

#     graph_id = runner.create_graph(graph)
#     return {"graph_id": graph_id}

# @app.post("/graph/run")
# def run_graph(req: RunRequest):
#     run_id, final_state, log = runner.run(req.graph_id, req.state)
#     return {"run_id": run_id, "state": final_state, "log": log}

# @app.get("/graph/state/{run_id}")
# def get_state(run_id: str):
#     return runner.runs.get(run_id, {})

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333


# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# templates = Jinja2Templates(directory="app/templates")


# from app.engine.graph import Graph
# from app.engine.runner import runner
# from app.engine.registry import tool_registry
# from app.workflows import code_review

# app = FastAPI()

# templates = Jinja2Templates(directory="app/templates")


# # -------------------------------
# #     API MODELS
# # -------------------------------
# class CreateGraphRequest(BaseModel):
#     nodes: dict
#     edges: dict


# class RunRequest(BaseModel):
#     graph_id: str
#     state: dict


# # -------------------------------
# #     UI ROUTES
# # -------------------------------

# @app.get("/", response_class=HTMLResponse)
# def ui_home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/tools", response_class=HTMLResponse)
# def ui_tools(request: Request):
#     return templates.TemplateResponse("tools.html", {"request": request, "tools": tool_registry.tools})


# @app.post("/run-workflow", response_class=HTMLResponse)
# def ui_run_workflow(request: Request, code: str = Form(...)):
#     # Define graph
#     graph = Graph()
#     for fn_name in ["extract_functions", "check_complexity", "detect_issues", "suggest_improvements"]:
#         graph.add_node(fn_name, getattr(code_review, fn_name))

#     graph.add_edge("extract_functions", "check_complexity")
#     graph.add_edge("check_complexity", "detect_issues")
#     graph.add_edge("detect_issues", "suggest_improvements")

#     # Run
#     graph_id = runner.create_graph(graph)
#     run_id, final_state, log = runner.run(graph_id, {"code": code, "threshold": 8})

#     return templates.TemplateResponse(
#         "run_workflow.html",
#         {"request": request, "state": final_state, "log": log},
#     )


# # -------------------------------
# #     API ROUTES
# # -------------------------------

# @app.post("/graph/create")
# def create_graph(req: CreateGraphRequest):
#     graph = Graph()

#     for name in req.nodes:
#         fn = getattr(code_review, name)
#         graph.add_node(name, fn)

#     for src, dst in req.edges.items():
#         graph.add_edge(src, dst)

#     graph_id = runner.create_graph(graph)
#     return {"graph_id": graph_id}


# @app.post("/graph/run")
# def run_graph(req: RunRequest):
#     run_id, final_state, log = runner.run(req.graph_id, req.state)
#     return {"run_id": run_id, "state": final_state, "log": log}


# @app.get("/graph/state/{run_id}")
# def get_state(run_id: str):
#     return runner.runs.get(run_id, {})


# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})



#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.engine.graph import Graph
from app.engine.runner import runner
from app.engine.registry import tool_registry
from app.workflows import code_review

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# ---------------- UI ROUTES ---------------- #

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tools", response_class=HTMLResponse)
def show_tools(request: Request):
    return templates.TemplateResponse(
        "tools.html",
        {"request": request, "tools": list(tool_registry.tools.keys())},
    )


@app.post("/tools/run", response_class=HTMLResponse)
def run_tool(request: Request, tool_name: str = Form(...), value: int = Form(...)):
    tool = tool_registry.get(tool_name)
    result = tool(value)
    return templates.TemplateResponse(
        "tools.html",
        {"request": request, "tools": list(tool_registry.tools.keys()), "result": result},
    )


@app.get("/workflow", response_class=HTMLResponse)
def workflow_ui(request: Request):
    return templates.TemplateResponse("workflow.html", {"request": request})


@app.post("/workflow/run", response_class=HTMLResponse)
def run_workflow(request: Request, code: str = Form(...), threshold: int = Form(...)):
    # Build graph
    graph = Graph()
    graph.add_node("extract_functions", code_review.extract_functions)
    graph.add_node("check_complexity", code_review.check_complexity)
    graph.add_node("detect_issues", code_review.detect_issues)
    graph.add_node("suggest_improvements", code_review.suggest_improvements)

    graph.add_edge("extract_functions", "check_complexity")
    graph.add_edge("check_complexity", "detect_issues")
    graph.add_edge("detect_issues", "suggest_improvements")

    state = {"code": code, "threshold": threshold}
    run_id, final_state, log = runner.run(runner.create_graph(graph), state)

    return templates.TemplateResponse(
        "workflow.html",
        {
            "request": request,
            "state": final_state,
            "log": log,
        },
    )


@app.get("/api", response_class=HTMLResponse)
def api_test(request: Request):
    return templates.TemplateResponse("api_test.html", {"request": request})


# ------------- FASTAPI ENDPOINTS (ORIGINAL REQUIREMENT) ------------ #

class CreateGraphRequest(dict):
    pass

class RunRequest(dict):
    pass


@app.post("/graph/create")
def create_graph(req: dict):
    graph = Graph()
    for name in req["nodes"]:
        fn = getattr(code_review, name)
        graph.add_node(name, fn)

    for src, dst in req["edges"].items():
        graph.add_edge(src, dst)

    graph_id = runner.create_graph(graph)
    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph(req: dict):
    run_id, final_state, log = runner.run(req["graph_id"], req["state"])
    return {"run_id": run_id, "state": final_state, "log": log}


@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return runner.runs.get(run_id, {})



@app.get("/graph-engine", response_class=HTMLResponse)
def graph_engine_ui(request: Request):
    # Build a demo graph (same as code review workflow)
    graph = Graph()
    graph.add_node("extract_functions", code_review.extract_functions)
    graph.add_node("check_complexity", code_review.check_complexity)
    graph.add_node("detect_issues", code_review.detect_issues)
    graph.add_node("suggest_improvements", code_review.suggest_improvements)

    graph.add_edge("extract_functions", "check_complexity")
    graph.add_edge("check_complexity", "detect_issues")
    graph.add_edge("detect_issues", "suggest_improvements")

    nodes = list(graph.nodes.keys())
    edges = graph.edges

    return templates.TemplateResponse(
        "graph_engine.html",
        {
            "request": request,
            "nodes": nodes,
            "edges": edges,
        }
    )
