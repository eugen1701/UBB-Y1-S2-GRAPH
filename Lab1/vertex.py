from __future__ import annotations

from typing import Optional

from edge import Edge, EdgeIteratorDirection, EdgeIterator


class Vertex:
    """
    Class that defines a Vertex
    """

    first_in: Optional[Edge]  # First Edge in the list that arrives to this vertex
    first_out: Optional[Edge]  # First Edge in the list that leaves from this vertex
    id: int

    def __init__(self, vid: int):
        self.id = vid
        self.first_in = None
        self.first_out = None

    def get_outbound_iterator(self) -> EdgeIterator:
        """
        Returns an iterator to iterate over all the edges that leave from this Vertex
        It's just and EdgeIterator that starts from the first edge that
        leaves the vertex in the "NEXT_SOURCE" direction
        """
        if self.first_out is None:
            return EdgeIterator(None, EdgeIteratorDirection.NEXT_SOURCE)
        return self.first_out.get_iter(EdgeIteratorDirection.NEXT_SOURCE)

    def get_inbound_iterator(self) -> EdgeIterator:
        """
        Returns an iterator to iterate over all the edges that leave from this Vertex
        It's just and EdgeIterator that starts from the first edge that
        arrives into the vertex in the "NEXT_TARGET" direction
        """
        if self.first_in is None:
            return EdgeIterator(None, EdgeIteratorDirection.NEXT_TARGET)
        return self.first_in.get_iter(EdgeIteratorDirection.NEXT_TARGET)
