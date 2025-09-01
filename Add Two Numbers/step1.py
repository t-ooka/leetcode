# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       dummy = ListNode(-1)
       dummy.next = l1
       rounded_up_number = 0

       while l1 and l2:
         rounded_up_number = (l1.val + l2.val) // 10
         l1.val = ((l1.val + l2.val) % 10) + rounded_up_number
         l1 = l1.next
         l2 = l2.next
       return dummy.next
      
