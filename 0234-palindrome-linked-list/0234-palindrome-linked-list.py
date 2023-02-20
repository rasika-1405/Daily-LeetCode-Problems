# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            curr = head
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        if head is None:
            return False
        
        # find the mid
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        head2 = reverse(slow)
        # slow.next = None
        curr = head
        
        while curr != None and head2 != None:
            if curr.val != head2.val:
                return False
            curr = curr.next
            head2 = head2.next
            
        return True