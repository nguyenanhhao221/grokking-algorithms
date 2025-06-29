from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T):
        self.items.insert(0, item)

    # NOTE: because Python use List underly for this, pop will actually O(n)
    # because after we pop a list, we need to move other element, however, optimize version can be done to make it actually O(1)
    # as the actual Queue
    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)
