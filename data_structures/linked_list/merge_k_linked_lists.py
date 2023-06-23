from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLinkedLists(self, listNodes: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(listNodes) == 0:
            return None

        while len(listNodes) > 1:
            mergedLists = list()
            for i in range(0, len(listNodes), 2):
                list1 = listNodes[i]
                list2 = listNodes[i+1] if (i+1) < len(listNodes) else None
                mergedLists.append(self.mergeTwoLinkedLists(list1, list2))
                print(f"[INFO] {mergedLists}")
            listNodes = mergedLists
        return listNodes[0]
    
    def mergeTwoLinkedLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail = list1
        if list2:
            tail = list2

        return dummy.next


if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    lists = [head1, head2, head3]
    
    s = Solution()
    merged_ll = s.mergeKLinkedLists(lists)
    print(merged_ll.val)

    while merged_ll:
        print(merged_ll.val, end="")
        merged_ll = merged_ll.next
