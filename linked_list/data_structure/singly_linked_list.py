from typing import Any


class ListNode:
    def __init__(self, val: Any = 0) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: Any) -> None:
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data: Any) -> None:
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, idx: int, data: Any) -> None:
        new_node = ListNode(data)
        if idx == 0:
            self.prepend(data)
        else:
            current = self.head
            for _ in range(idx - 1):
                if not current:
                    return

                current = current.next
                new_node.next = current.next
                current.next = new_node

    def delete(self, idx: int, data: Any) -> None:
        if idx == 0 and self.head is not None:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx - 1):
                if not current:
                    return
                current = current.next

            if current is not None and current.next is not None:
                current.next = current.next.next
