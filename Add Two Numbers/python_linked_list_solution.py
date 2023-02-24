# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1=0
        num_2=0
        l3 = ListNode()
        item_cur = l1
        place = 10 
        while item_cur is not None:
            num_1 += item_cur.val * place // 10
            place *= 10
            item_cur = item_cur.next
        place = 10
        item_cur = l2
        while item_cur is not None:
            num_2 += item_cur.val * place // 10
            place *= 10
            item_cur = item_cur.next
        sum = num_1+num_2
        print(sum)
        l3 = ListNode(sum % 10)
        sum=sum//10
        while sum > 0:
            temp =l3
            l3 = ListNode(sum %10, temp)
            sum=sum//10
        print(l3)
        prev = None 
        curr = l3
        following = l3

        while curr is not None:
            following = following.next
            curr.next = prev
            prev = curr
            curr = following
        return prev