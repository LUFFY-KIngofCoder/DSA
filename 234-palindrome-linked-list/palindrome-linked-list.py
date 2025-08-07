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

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # reach middle of list
        
        first = head
        new_head = reversell(slow)
        second = new_head


        while second != None:
            if first.val != second.val:
                reversell(new_head)
                return False
            second =second.next
            first = first.next
        return True