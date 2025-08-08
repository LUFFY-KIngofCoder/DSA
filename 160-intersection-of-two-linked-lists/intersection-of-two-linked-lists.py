# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        b = []

        while headA != None or headB != None:
            if headA!= None:
                a.append(headA)
                if headA in b:
                    return headA
                headA = headA.next
                
            if headB!= None:
                b.append(headB)
                if headB in a:
                    return headB        
                headB = headB.next
        return 