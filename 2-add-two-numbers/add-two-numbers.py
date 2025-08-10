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
        start = head = None

        while a or b:
            if a and b:
                val = a.val+b.val+c
            elif not a:
                val = b.val+c
            elif not b: 
                val = a.val+c
            print(val, val%10, val//10)
            if not head:
                head = ListNode(val%10)
                start = head
            else:
                head.next = ListNode(val%10)
                head = head.next
            c = val//10
            if a:
                a = a.next
            if b:
                b = b.next
        if c!=0 :
            head.next = ListNode(c)
        return start

