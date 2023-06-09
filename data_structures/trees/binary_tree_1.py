class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start: Node, traversal: str) -> str:
        if start:
            traversal += (str(start.val) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start: Node, traversal: str) -> str:
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.val) + "-")
        return traversal

    def inorder_print(self, start: Node, traversal: str) -> str:
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.val) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    print(tree.print_tree("postorder"))
