Mini Workflow Engine – Code Review & Tool Execution Platform (FastAPI)

This project is a **lightweight Workflow Engine** built using **FastAPI**, featuring:

* A **Graph-based execution engine**
* A **registry system** for pluggable tools
* A **Code Review Workflow** (functions → complexity → issues → improvements)
* A **simple UI** using HTML + Jinja templates
* Built-in **API tester** for endpoints
* A **Graph Viewer** to visualize workflow execution order

This serves as a **submission** demonstrating workflow orchestration, modularity, execution tracing, and minimal UI  presentation.

---

# ✨ Features Overview

## . Workflow Engine (Core Logic)

A minimal agent/workflow engine consisting of:

### **Graph Engine (`graph.py`)**

* Nodes = Python functions
* Edges define execution order
* Can run any directed acyclic pipeline

### **Runner (`runner.py`)**

* Executes graph nodes step-by-step
* Maintains a **run state**
* Stores **execution logs**
* Supports **run id** + **state retrieval**

### **Tool Registry (`registry.py`)**

* Lets you register Python functions as tools
* Tools can be dynamically executed via UI

Tools added:

* `double(x)` – returns x*2
* `triple(x)` – returns x*3
* `square(x)` – returns x²

---

##  2. Code Review Workflow Module

Located in: `app/workflows/code_review.py`

Pipeline Nodes:

1. **extract_functions** – parses Python functions
2. **check_complexity** – counts branches, loops
3. **detect_issues** – finds unused variables, prints, etc.
4. **suggest_improvements** – gives recommendations

This workflow is fully automated using the Graph Engine.

---

##  3. UI (FastAPI + Jinja Templates)

Beautiful, clean HTML pages:

### **Home Page**

* View Tool Registry
* Code Review Workflow
* Test API Endpoints
* View Graph Engine

### **Tool Registry Page**

* Shows available tools
* Run a tool with input
* Clean readable output

### **Code Review Workflow Page**

* Paste Python code
* Enter complexity threshold
* Shows:

  * Extracted functions
  * Complexity score
  * Issues detected
  * Suggested improvements
  * Execution Log

### **API Tester**

Buttons for:

* `/graph/create`
* `/graph/run`
* `/graph/state/{id}`

No Postman required.

### **Graph Engine Viewer**

Displays:

* All nodes
* All edges
* Execution order
* Human-readable flow diagram

---

# 📁 Project Structure

```
TREDENCE/
├── app/
│   ├── engine/
│   │   ├── graph.py
│   │   ├── registry.py
│   │   └── runner.py
│   ├── workflows/
│   │   └── code_review.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── tools.html
│   │   ├── workflow.html
│   │   ├── api_test.html
│   │   └── graph_engine.html
│   ├── static/
│   │   └── style.css
│   └── main.py
└── README.md
```

---

# ⚙️ Installation & Setup

### **1 Clone Repo**

```sh
git clone https://github.com/pmpgowthami2k4/TREDENCE.git
cd TREDENCE
```

### **2 Create Virtual Environment (Optional but recommended)**

Windows:

```sh
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### **3 Install Dependencies**

```sh
pip install fastapi uvicorn jinja2 python-multipart
```

### **4 Run Application**

```sh
uvicorn app.main:app --reload
```

App will run on:

```
http://127.0.0.1:8000
```

---

#  Using the UI

## **🔹 Tool Registry**

Navigate to:

```
/tools
```

You can:

* Select tool → double / triple / square
* Enter a number
* See the readable result

---

## **🔹 Code Review Workflow**

Navigate to:

```
/workflow
```

Paste sample Python code:

```python
def add(a, b):
    return a + b

def process(x):
    if x > 10:
        print("Large")
    return x * 2

def unused_function():
    temp = 5
```

Output includes:

* Extracted functions
* Complexity score
* Issues found
* Suggested improvements
* Execution log

---

## **🔹 API Endpoint Tester**

Navigate to:

```
/api
```

Buttons for:

* `/graph/create`
* `/graph/run`
* `/graph/state/{run_id}`

---

## **🔹 Graph Viewer**

Navigate to:

```
/graph-engine
```

It will show:

* Nodes
* Edges
* Execution flow diagram

---

#  API Documentation

### **POST /graph/create**

Creates a workflow graph.

```json
{
  "nodes": ["extract_functions", "check_complexity"],
  "edges": { "extract_functions": "check_complexity" }
}
```

Returns:

```json
{ "graph_id": "<uuid>" }
```

---

### **POST /graph/run**

Runs a graph.

```json
{
  "graph_id": "...",
  "state": {"code": "..."}
}
```

---

### **GET /graph/state/{run_id}**

Retrieve execution logs + final state.

---

#  Running Everything End-to-End

1. Start server:

   ```
   uvicorn app.main:app --reload
   ```
2. Visit:

   ```
   http://127.0.0.1:8000
   ```
3. Explore:

   * Tools
   * Code Review Workflow
   * API Tester
   * Graph Engine

#  Screenshots of the work

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0fb820bb-417c-4784-99af-9d3a3b8ff10b" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ba74d3d4-c56e-4321-b91b-ec8758f316ab" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ebaa47da-32d6-49d4-819c-1786123b5a63" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bf12ce3e-b2f4-4ab9-bd6e-0e240d8b60b2" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f8dd2619-0c9a-4379-bc10-bfc2d662f167" />





