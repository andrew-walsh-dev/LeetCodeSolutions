# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1 = str(l1.val)
        str2 = str(l2.val)
        
        while l1.next is not None:
            l1 = l1.next
            str1 += str(l1.val)
        str1 = str1[::-1]
        
        while l2.next is not None:
            l2 = l2.next
            str2 += str(l2.val)
        str2 = str2[::-1]
        
        sum = str(int(str1) + int(str2))
        
        
        prev = None
        for idx in range(len(sum)):
                if prev is None:
                    node = ListNode(sum[idx], None)
                    prev = node
                else:
                    node = ListNode(sum[idx], prev)
                    prev = node
        return node