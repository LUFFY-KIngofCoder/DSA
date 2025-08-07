# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast , slow = head
        pos = {}
        c= 0
        while head:
            if head in pos:
                return head
            else:
                pos[head] = c
            c+=1
            head = head.next
        
        return 