from typing import Dict, Callable, Optional

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Callable] = {}
        self.edges: Dict[str, str] = {}
        self.start_node: Optional[str] = None

    def add_node(self, name: str, fn: Callable):
        self.nodes[name] = fn
        if not self.start_node:
            self.start_node = name

    def add_edge(self, src: str, dst: str):
        self.edges[src] = dst

    def get_next(self, node_name: str):
        return self.edges.get(node_name)
