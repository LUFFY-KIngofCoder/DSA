# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 1
        count = head
        while count.next:
            n+=1
            count = count.next
        end = count
        k = k%n    
        
        if k == 0 :
            return head

        move = n - (k%n)
        start = head
        new_head = None 
        while move-1 > 0:
            head = head.next
            move-=1
        
        new_head = head.next
        head.next = None
        end.next = start

        return new_head



            



