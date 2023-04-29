from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_vals = []
        current = head
        while current:
            node_vals.append(current.val)
            current = current.next

        return node_vals == node_vals[::-1]

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    solution_obj = Solution()
    print(solution_obj.isPalindrome(head))
