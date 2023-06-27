from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self,  p: Optional[Node], q: Optional[Node]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    # first
    first_tree = Node(1, left=Node(2), right=Node(3))
    # second
    second_tree = Node(1, left=Node(2), right=Node(3))

    solution_obj = Solution()
    print(solution_obj.isSameTree(first_tree, second_tree))
