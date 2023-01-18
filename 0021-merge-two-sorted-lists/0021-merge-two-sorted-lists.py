# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # using 3 pointers
        sorted_list = curr = ListNode()
        p_pointer = list1
        q_pointer = list2
        
        while p_pointer and q_pointer:
            if p_pointer.val < q_pointer.val:
                curr.next = p_pointer
                p_pointer = p_pointer.next
            else:
                curr.next = q_pointer
                q_pointer = q_pointer.next
            curr = curr.next
        
        if p_pointer:
            curr.next = p_pointer
        if q_pointer:
            curr.next = q_pointer
        return sorted_list.next