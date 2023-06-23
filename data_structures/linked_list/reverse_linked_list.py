from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur:
            # reverse the link
            cur.next = prev
            # prepare to move to the next node
            # by assigning the cur value to the
            # pre value
            prev = cur
            # move to the next node
            cur = cur.next
            print(cur)
        return prev

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s = Solution()
    s.reverseLinkedList(head)
