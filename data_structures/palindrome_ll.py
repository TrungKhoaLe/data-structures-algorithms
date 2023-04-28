from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow = fast = head
        i = 0
        while fast and fast.next:
            print(i)
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow

        # reverse the linked list
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)
    solution_obj = Solution()
    print(solution_obj.isPalindrome(head))
