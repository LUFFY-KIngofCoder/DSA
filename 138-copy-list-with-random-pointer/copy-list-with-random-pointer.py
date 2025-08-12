"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # h = {}
        # dummy = Node(0)
        # new_head = dummy
        # org_start = head
        # while head: 
        #     new_head.next = Node(head.val)
        #     new_head = new_head.next
        #     h[head] = new_head
        #     head = head.next
        # new_head = dummy.next

        # for i in h:
        #     if i.random:
        #         h[i].random = h[i.random]
        
        # return new_head

        start = head
        while head:
            a = Node(head.val)
            a.next = head.next
            head.next = a

            head = head.next.next
        head = start 

        while head:
            head.next.random = head.random.next if head.random else None
            head = head.next.next

        head = start
        dummy = Node(-1)
        start = dummy

        while head:
            start.next = head.next
            head.next = head.next.next
            head = head.next
            start = start.next
        
        return dummy.next