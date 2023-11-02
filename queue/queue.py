from typing import Any


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data: Any) -> None:
        self.items.append(data)

    def dequeue(self) -> int:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)
