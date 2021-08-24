# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None: 
            return
        
        list = []
        while l1 is not None:
            list.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list.append(l2.val)
            l2 = l2.next
        list.sort()
        
        next = ListNode(list[len(list) - 1])
        for i in range(len(list) - 2, -1, -1):
            curr = ListNode(list[i], next)
            next = curr
        return next