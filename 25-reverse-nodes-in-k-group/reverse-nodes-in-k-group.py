# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    if not head or not head.next:
        return head,head
    
    new_head, _ = reverse(head.next)

    front = head.next
    front.next = head
    head.next = None

    return new_head , head 

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
                return head 
        
        
        new_head = None
        prev = None
        start = head
        end = None
        count = 0 
        while head:                       
            count+=1
            print(head.val)
            if count == k:    
                end , head = head, head.next
                end.next = None
                l,r = reverse(prev.next if prev else start )
                if prev:
                    prev.next = l
                else:
                    new_head = l
                r.next = head
                prev = r
                count = 1 
            if head: 
                head= head.next

        return new_head