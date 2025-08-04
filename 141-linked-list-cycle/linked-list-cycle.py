# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # h = []       
        # while head != None:
        #     if head in h:
        #         return True
        #     h.append(head)
        #     head = head.next

        # return False
        #-----------------------------
        fast,slow = head,head
        print(head.val if head  else "")
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False