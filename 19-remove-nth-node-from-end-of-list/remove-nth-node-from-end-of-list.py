# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reversell(head):
    if not head or not head.next:
        return head
    new_head = reversell(head.next)

    front = head.next

    front.next = head

    head.next = None
    
    return new_head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return 

        new_head = reversell(head)
        s  = new_head
        
        prev = None
        while n!=1:
            n-=1
            prev = new_head
            new_head = new_head.next
        
        print(new_head.val)
        if prev == None:
            s = new_head.next
        else:
            prev.next = new_head.next
            new_head.next = None
        
        head = reversell(s)

        return head

