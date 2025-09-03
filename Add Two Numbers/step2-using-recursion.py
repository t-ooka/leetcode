# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:
            return None
        
        value_1 = l1.val if l1 else 0
        value_2 = l2.val if l2 else 0

        carry, remainder = divmod(value_1 + value_2 + carry, 10)

        next_node = self.add(
          l1.next if l1 else None,
          l2.next if l2 else None,
          carry
        )

        return ListNode(remainder, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
        
