import uuid

class WorkflowRunner:
    def __init__(self):
        self.graphs = {}
        self.runs = {}

    def create_graph(self, graph_def):
        graph_id = str(uuid.uuid4())
        self.graphs[graph_id] = graph_def
        return graph_id

    def run(self, graph_id, state):
        graph = self.graphs[graph_id]
        current = graph.start_node
        log = []

        while current:
            fn = graph.nodes[current]
            state = fn(state)

            log.append(f"Executed: {current}")

            if state.get("quality_score", 0) >= state.get("threshold", 10):
                log.append("Quality threshold met. Stopping.")
                break

            current = graph.get_next(current)

        run_id = str(uuid.uuid4())
        self.runs[run_id] = state
        return run_id, state, log


runner = WorkflowRunner()
