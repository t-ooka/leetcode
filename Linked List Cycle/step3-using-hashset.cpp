/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
      unordered_set<ListNode*> seen_nodes;
      ListNode* node = head;

      while (node != nullptr) {
        if (seen_nodes.contains(node)) {
          return true;
        }
        seen_nodes.insert(node);
        node = node->next;
      } 
      return false;
    }
};
