from __future__ import annotations

import typing
from enum import Enum

if typing.TYPE_CHECKING:
    from vertex import Vertex
    from typing import Optional


class Edge:
    """
    A class that represents an edge
    """

    source: Vertex  # Vertex from which the edge leaves
    target: Vertex  # Vertex into which the edge arrives
    value: int  # The Cost of the Edge
    next_source: Optional[Edge]  # The next Edge that leaves from the same source vertex, if it's None it means this
    # edge is the last element in the list of edges that leave from the same source vertex
    previous_source: Optional[Edge]  # The previous Edge that leaves from the same source vertex, if it's None it
    # means this edge is the first element in the list of edges that leave from the same source vertex
    next_target: Optional[Edge]  # The next Edge that arrives to the same target vertex, if it's None it
    # means this edge is the last element in the list of edges that arrive to the same target vertex
    previous_target: Optional[Edge]  # The previous Edge that arrives to the same target vertex, if it's None it

    # means this edge is the last element in the list of edges that arrive to the same target vertex

    def __init__(self, source: Vertex, target: Vertex, value: int):
        self.source = source
        self.target = target
        self.value = value
        self.next_source = None
        self.previous_source = None
        self.next_target = None
        self.previous_target = None

    def get_iter(self, direction: EdgeIteratorDirection) -> EdgeIterator:
        """
        Returns an iterator to iterate over the linked edges
        :param direction: The Direction in which to iterate
        """
        return EdgeIterator(self, direction)


class EdgeIteratorDirection(str, Enum):
    """
    Specifies in which direction to iterate
    """

    NEXT_SOURCE = "next_source"
    PREV_SOURCE = "previous_source"
    NEXT_TARGET = "next_target"
    PREV_TARGET = "previous_target"


class EdgeIterator:
    """
    An Iterator for the Linked lists of an Edge
    """

    def __init__(self, starting_edge: Optional[Edge], direction: EdgeIteratorDirection):
        self.current_edge: Optional[Edge] = starting_edge
        self.direction = direction

    def __iter__(self) -> EdgeIterator:
        return self

    def __next__(self) -> Edge:
        if self.current_edge is None:
            raise StopIteration
        old_edge = self.current_edge
        self.current_edge = getattr(old_edge, self.direction.value)
        return old_edge
