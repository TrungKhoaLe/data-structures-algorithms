"""
A binary search tree (BST) is a binary tree data structure in which each
new_node has at least two child new_nodes. All values in the left subtree are less
than the value of the new_node. All values in the right subtree are greater than
value of the new_node.
"""
from typing import Any


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data: Any) -> None:
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                # insert to the left
                if data < current.data:
                    # if the left node is None
                    if not current.left:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                # insert to the right
                else:
                    # if the right node is None
                    if not current.right:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def insert_recursive(self, data: Any):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, root: TreeNode, data: Any):
        if not root:
            return TreeNode(data)
        else:
            if data < root.data:
                root.left = self._insert_recursive(root.left, data)
            else:
                root.right = self._insert_recursive(root.right, data)
        return root

    def printTree(self, current: TreeNode, level: int = 0):
        if current:
            self.printTree(current.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(current.data))
            self.printTree(current.right, level + 1)


if __name__ == "__main__":
    bst = BinaryTree()
    bst.insert_recursive(50)
    bst.insert_recursive(29)
    bst.insert_recursive(20)
    bst.insert_recursive(40)
    bst.insert_recursive(70)
    bst.insert_recursive(60)
    bst.printTree(bst.root)
