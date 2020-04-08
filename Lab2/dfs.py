from typing import Dict

from graph import Graph
from vertex import Vertex


def dfs_main(graph: Graph):
    max_flag = 0
    flags: Dict[int, int] = {}
    for i in range(graph.count_vertex()):
        flags[i] = -1
    for vertex in graph.get_vertex_iterator():
        if flags[vertex.id] == -1:
            max_flag += 1
            flags[vertex.id] = max_flag
            dfs(vertex, max_flag, flags)
    for i in range(1, max_flag + 1):
        something_matched = False
        string_buffer = ""
        for item in flags.items():
            if item[1] == i:
                something_matched = True
                string_buffer += str(item[0]) + ", "
        if something_matched:
            print(i, ": ", string_buffer)


def dfs(vertex: Vertex, flag: int, flags: Dict[int, int]):
    for edge in vertex.get_outbound_iterator():
        if flags[edge.target.id] == -1:
            flags[edge.target.id] = flag
            dfs(edge.target, flag, flags)
