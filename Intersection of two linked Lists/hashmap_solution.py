# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersection = {}
        # loop through linked list
        while headA:
            intersection[headA]=1
            headA = headA.next
        while headB:
            if headB in intersection:
                return headB
            headB = headB.next 
        return None