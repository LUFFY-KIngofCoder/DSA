# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # a = ""
        # while head!=None:
        #     a= a+str(head.val)
        #     head = head.next
        # if a == a[::-1]:
        #     return True
        # else:
        #     return False

        slow,fast = head,head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next # reach middle of list

        if fast.next!= None:
            fast = fast.next
        slow = slow.next
        
        a = None
        while slow != None:
            temp = slow.next
            slow.next = a
            a = slow
            slow = temp
        ans = True
        while fast != None:
            if head.val != fast.val:
                return False
            fast =fast.next
            head = head.next
        return True