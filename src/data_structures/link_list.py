from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val: T = val
        self.next: Node[T] | None = None

    def set_next(self, node: "Node[T] | None") -> None:
        self.next = node
