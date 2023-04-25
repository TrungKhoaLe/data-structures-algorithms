class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:

        if index < 0:
            return -1

        current = self.head 
        for _ in range(index):
            if current is None:
                return -1
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index < 0:
            self.addAtHead()
            return
        current = self.head
        prev = None
        for _ in range(index):
            if current is None:
                return
            prev = current
            current = current.next
        new_node.next = current
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        current = self.head
        for _ in range(index):
            if current is None:
                return
            prev = current
            current = current.next

        prev.next = current.next
