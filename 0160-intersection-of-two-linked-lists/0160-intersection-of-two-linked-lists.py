# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0
        countB = 0
        
        curr = headA
        
        while curr != None:
            countA += 1
            curr = curr.next
            
        curr = headB
        
        while curr != None:
            countB += 1
            curr = curr.next
            
        if countA > countB:
            front = headA
            for i in range(countA-countB):
                front = front.next
            
            back = headB
            while front!=back:
                front = front.next
                back = back.next
                
            return back
        else:
            front = headB
            for i in range(countB-countA):
                front = front.next
            
            back = headA
            while front!=back:
                front = front.next
                back = back.next
                
            return back