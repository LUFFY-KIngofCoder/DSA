# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    if not head or not head.next:
        return head
    new_head = reverse(head)
    head.next.next = head.next
    head.next = None
    return new_head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a , b = l1,l2
        c = 0
        start = head = ListNode()

        while a or b or c:
            v1 = a.val if a else 0
            v2 = b.val if b else 0
            val = v1+v2+c 
            head.next = ListNode(val%10)
            head = head.next
            c = val//10
            a = a.next if a else None
            b = b.next if b else None

        # if c!=0 :
        #     head.next = ListNode(c)
        return start.next

