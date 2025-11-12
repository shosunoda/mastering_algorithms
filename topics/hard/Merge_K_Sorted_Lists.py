from heapq import heappush,  heappop 
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # i mean, for me we can grab all the values, have it sorted, and then construct a new linkedlist based on this
        # this requires the use of heap datastructure for sorting
        # thats it i think?
        min_heap = []
        for head in lists:
            while head != None:
                heappush(min_heap, head.val)
                head = head.next
        new_head = ListNode()
        dummy = new_head
        while min_heap:
            next_node = ListNode(val = heappop(min_heap))
            dummy.next = next_node
            dummy = dummy.next
        return new_head.next
            


        