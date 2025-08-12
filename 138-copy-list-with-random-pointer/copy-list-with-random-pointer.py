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
        h = {}
        dummy = Node(0)
        new_head = dummy
        org_start = head
        while head: 
            new_head.next = Node(head.val)
            new_head = new_head.next
            h[head] = new_head
            head = head.next
        new_head = dummy.next

        for i in h:
            if i.random:
                h[i].random = h[i.random]
        
        return new_head
