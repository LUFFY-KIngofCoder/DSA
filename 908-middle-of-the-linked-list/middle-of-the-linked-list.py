# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        count= 0 
        a = head
        while a!= None:
            a = a.next
            count+=1
        mid = count//2
        while mid!= 0:
            head = head.next
            mid-=1
        return head
