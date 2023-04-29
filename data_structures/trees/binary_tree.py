from typing import Any


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insetr(self, val: Any) -> None:
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            curr = self.root
            while True:
                # insert to the left
                if val < curr.val:
                    if not curr.left:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                # insert to the right
                else:
                    if not curr.right:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    def search(self, val: Any) -> bool:
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False
