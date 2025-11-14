from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        l1, l2 = list1, list2
        while l1 and l2:
            if l2.val < l1.val:
                dummy.next = ListNode(val =l2.val)
                l2 = l2.next
            else:
                dummy.next = ListNode(val = l1.val)
                l1 = l1.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2

        return head.next

        