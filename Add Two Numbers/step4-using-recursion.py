# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self, node1: Optional[ListNode], node2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if node1 is None and node2 is None and carry == 0:
            return None
        value1 = node1.val if node1 else 0
        value2 = node2.val if node2 else 0
        carry, remainder = divmod(value1 + value2 + carry , 10)

        next_node = self.add(
          node1.next if node1 else None,
          node2.next if node2 else None,
          carry
        )

        return ListNode(remainder, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
        
