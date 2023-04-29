from typing import Optional


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head, None)
        if self.head:
            self.head.prev = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, None, self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            new_node = ListNode(val, curr, curr.prev)
            curr.prev.next = new_node
            curr.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for i in range(index):
            curr = curr.next
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        self.size -= 1
