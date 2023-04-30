class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_bst(self, root: Node) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            elif node.val <= min_val or node.val >= max_val:
                return False
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)

        return helper(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    # Testcase 1:
    tree1 = Node(3)
    tree1.left = Node(2)
    tree1.right = Node(4)
    solution_obj = Solution()
    print(solution_obj.is_bst(tree1))
    # Test case 3
    tree3 = Node(3)
    tree3.left = Node(4)
    tree3.right = Node(2)
    print(solution_obj.is_bst(tree3))  # expected output: False
