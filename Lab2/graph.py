from __future__ import annotations

import copy
from typing import Dict, Iterator

from edge import Edge, EdgeIteratorDirection
from vertex import Vertex


class Graph:
    """
    Represents a directed graph
    """

    def __init__(self, number_of_vertices: int):
        self.vertices: Dict[int, Vertex] = {}
        for i in range(0, number_of_vertices):
            self.vertices[i] = Vertex(i)

    def count_vertex(self) -> int:
        """
        Number of vertices
        :return: int
        """
        return len(self.vertices)

    def get_vertex_iterator(self) -> Iterator[Vertex]:
        """
        Returns an iterator for iterating over every vertex in the graph
        :return: the vertex iterator
        """
        return iter(self.vertices.values())

    def insert_vertex(self):
        """
        Inserts a new vertex into the graph
        """
        self.vertices[self.count_vertex()] = Vertex(self.count_vertex())

    def remove_vertex(self, vertex_position: int) -> Vertex:
        """
        Erases the vertex and all the connected edges to other vertices
        and repositions the index of the last vertex over the erased one
        :param vertex_position:
        :return:
        """
        first_in = self.vertices[vertex_position].first_in
        first_out = self.vertices[vertex_position].first_out
        if first_out is not None:
            for edge in first_out.get_iter(EdgeIteratorDirection.NEXT_SOURCE):
                if edge.previous_target is not None:
                    edge.previous_target.next_target = edge.next_target
                else:
                    self.vertices[edge.target.id].first_in = edge.next_target
                if edge.next_target is not None:
                    edge.next_target.previous_target = edge.previous_target
        if first_in is not None:
            for edge in first_in.get_iter(EdgeIteratorDirection.NEXT_TARGET):
                if edge.previous_source is not None:
                    edge.previous_source.next_source = edge.next_source
                else:
                    self.vertices[edge.source.id].first_out = edge.next_source
                if edge.next_source is not None:
                    edge.next_source.previous_source = edge.previous_source
        self.vertices[vertex_position].first_in = None
        self.vertices[vertex_position].first_out = None
        removed_vertex = self.vertices[vertex_position]
        self.vertices[vertex_position] = self.vertices.pop(self.count_vertex() - 1)
        self.vertices[vertex_position].id = vertex_position
        return removed_vertex

    def insert_new_edge(self, source_vertex: int, target_vertex: int, value: int):
        """
        Inserts a new edge
        :param source_vertex: Index of vertex it leaves from
        :param target_vertex: Index of vertex it arrives into
        :param value: The Cost of the Edge
        """
        new_edge = Edge(self.vertices[source_vertex], self.vertices[target_vertex], value)
        source_edge = self.vertices[source_vertex].first_out
        target_edge = self.vertices[target_vertex].first_in
        if source_edge is None:
            self.vertices[source_vertex].first_out = new_edge
            new_edge.previous_source = None
            new_edge.next_source = None
        else:
            for source_edge in source_edge.get_iter(EdgeIteratorDirection.NEXT_SOURCE):
                pass
            source_edge.next_source = new_edge
            new_edge.previous_source = source_edge
            new_edge.next_source = None

        if target_edge is None:
            self.vertices[target_vertex].first_in = new_edge
            new_edge.previous_target = None
            new_edge.next_target = None
        else:
            for target_edge in target_edge.get_iter(EdgeIteratorDirection.NEXT_TARGET):
                pass
            target_edge.next_target = new_edge
            new_edge.previous_target = target_edge
            new_edge.next_target = None

    def delete_edge(self, source_vertex: int, target_vertex: int):
        # TODO add to return bool if remove was successful or not
        """
        Remvoes an edge, defined by the vertex where it leaves from and the vertex it arrives into
        :param source_vertex: Index of vertex it leaves from
        :param target_vertex: Index of vertex it arrives into
        """
        first_out = self.vertices[source_vertex].first_out
        if first_out is not None:
            for edge in first_out.get_iter(EdgeIteratorDirection.NEXT_SOURCE):
                if edge.target.id == target_vertex:
                    if edge.previous_source is not None:
                        edge.previous_source.next_source = edge.next_source
                    else:
                        self.vertices[source_vertex].first_out = edge.next_source
                    if edge.next_source is not None:
                        edge.next_source.previous_source = edge.previous_source
                    if edge.previous_target is not None:
                        edge.previous_target.next_target = edge.next_target
                    else:
                        self.vertices[target_vertex].first_in = edge.next_target
                    if edge.next_target is not None:
                        edge.next_target.previous_target = edge.previous_target
                    break

    def has_edge(self, source_vertex: int, target_vertex: int) -> bool:
        """
        Checks if an edge from Vertex A to Vertex B exists
        :param source_vertex: Index of Vertex A
        :param target_vertex: Index of Vertex B
        :return: True if edge exists, False otherwise
        """
        edge = self.vertices[source_vertex].first_out
        if edge is None:
            return False
        for edge in edge.get_iter(EdgeIteratorDirection.NEXT_SOURCE):
            if edge.target.id == target_vertex:
                return True
        return False

    def get_copy(self) -> Graph:
        """
        Returns a copy of the Graph
        :return:
        """
        return copy.deepcopy(self)
