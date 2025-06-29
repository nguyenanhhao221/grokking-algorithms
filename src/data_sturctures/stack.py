from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item


def is_balanced(input_str: str) -> bool:
    s = Stack[str]()
    for char in input_str:
        if char == "(":
            s.push(char)
        else:
            top_of_stack = s.peek()
            if top_of_stack != "(":
                return False
            _ = s.pop()

    return s.size() == 0


input = "()"
expect = True
output = is_balanced(input)

assert output == expect
