# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# l1 = [2,0,1] + l2 = [8,4,9] = 
# 2 -> 0 -> 1 
# 8 -> 4 -> 9
# 0 -> 5 -> 0 -> 1

# l1 = [9], l2 = [1,2,3]
# 9 -> 0 -> 0
# 1 -> 2 -> 3
# 0 -> 3 -> 3

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        # find length of input lists
        l1_pointer = l1
        l2_pointer = l2
        l1_len = 0
        while l1_pointer:
            l1_len+=1
            l1_pointer = l1_pointer.next
            
        l2_len = 0
        while l2_pointer:
            l2_len += 1
            l2_pointer = l2_pointer.next
            
        l1_copy = l1
        l2_copy = l2
            
        if l1_len != l2_len:
            n_zeros = abs(l1_len - l2_len)
            if l1_len < l2_len:
                l1c_pointer = l1_copy
                while l1c_pointer.next:
                    l1c_pointer = l1c_pointer.next
                for i in range(n_zeros):
                    l1c_pointer.next = ListNode()
                    l1c_pointer = l1c_pointer.next
            else:
                l2c_pointer = l2_copy
                while l2c_pointer.next:
                    l2c_pointer = l2c_pointer.next
                for i in range(n_zeros):
                    l2c_pointer.next = ListNode()
                    l2c_pointer = l2c_pointer.next
        
        p1 = l1_copy
        p2 = l2_copy
        l_out = ListNode()
        p3 = l_out
        l_sum = 0
        
        while p1:
            l_sum = p1.val + p2.val
            if carry:
                l_sum += 1
            if l_sum > 9:
                carry = True
            else:
                carry = False
            # p3.val = l_sum % 10
            p3.next = ListNode(l_sum % 10)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        if carry:
            num = l_sum // 10
            p3.next = ListNode(num)
        return l_out.next
        