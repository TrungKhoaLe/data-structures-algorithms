"""
Stack is a linear data structure that follows the LIFO principle. A stack has
one end, whereas a queue has two ends.
"""
from typing import Any


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data: Any) -> None:
        self.items.append(data)

    def pop(self) -> int:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)
