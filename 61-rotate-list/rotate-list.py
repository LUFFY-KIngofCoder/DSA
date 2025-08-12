# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        count = head
        end = count
        while count:
            n+=1
            end = count
            count = count.next
        k = k%n    
        if k == 0 or k==n:
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



            



