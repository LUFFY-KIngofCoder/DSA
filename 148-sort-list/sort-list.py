# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergesort(start , end):
    if start == end:
        return start

    slow,fast = start,start 
   
    while fast!= end and fast.next != end:
        slow = slow.next
        fast = fast.next.next

    rstart = slow.next
    slow.next = None
    end.next =None

    lstart = mergesort(start , slow)
    rstart = mergesort(rstart , end) 
    
    head = merge(lstart , rstart)
    return head


def merge(start,slow):
    l = start
    r = slow 
    head = None
    a = None

    while l != None and r!=None:
        if l.val <= r.val:
            if not a:
                head = l
                a = l
            else:
                a.next = l
                a = l
            l = l.next

        else:
            if not a:
                head = r
                a = r
            else:
                a.next = r
                a = r
            r = r.next

    while l != None:
        a.next = l
        a = l
        l = l.next

    while r != None:
        a.next = r 
        a = r
        r = r.next
    
    return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        end = head
        while end.next!=None: # type: ignore
            end = end.next # type: ignore
        
        head = mergesort(head,end)
        return head