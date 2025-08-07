# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pos = {}
        # c= 0
        # while head:
        #     if head in pos:
        #         return head
        #     else:
        #         pos[head] = c
        #     c+=1
        #     head = head.next
        
        # return 

        fast , slow = head, head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow!= fast:
                    fast =fast.next
                    slow = slow.next
                return slow
        
        return 
