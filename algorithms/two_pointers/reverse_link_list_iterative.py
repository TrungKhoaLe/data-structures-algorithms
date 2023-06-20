class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            # move prev and curr to new nodes
            prev = curr
            curr = nxt
        return prev


if __name__ == '__main__':
    # head = [1, 2, 3, 4, 5]
    list_node_head = ListNode(val=1)
    list_node_head.next = ListNode(val=2)
    list_node_head.next.next = ListNode(val=3)
    list_node_head.next.next.next = ListNode(val=4)
    list_node_head.next.next.next.next = ListNode(val=5)
    s = Solution()
    new_head = s.reverseLinkList(list_node_head)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
