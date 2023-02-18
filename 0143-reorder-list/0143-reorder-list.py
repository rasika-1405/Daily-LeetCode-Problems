# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev = None
            curr = head
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        
        # find mid using fast & slow pointers
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        head2 = reverse(slow.next)
        
        slow.next = None
        curr = head
        
        # Merge
        
        while head2 != None:
            temp = curr.next
            curr.next = head2
            head2 = head2.next
            curr.next.next = temp
            curr = temp
            