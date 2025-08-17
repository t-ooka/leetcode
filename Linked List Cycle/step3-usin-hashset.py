# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      seen_nodes = set() 
      node = head

      while node:
        if node in seen_nodes:
          return True
        seen_nodes.add(node)
        node = node.next

      return False
