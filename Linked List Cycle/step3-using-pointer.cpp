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
      ListNode* fast_node = head;
      ListNode* slow_node = head;

      while (fast_node != nullptr && fast_node->next != nullptr) {
        slow_node = slow_node->next;
        fast_node = fast_node->next->next;

        if (slow_node == fast_node) {
          return true;
        }
      } 
      return false;
    }
}
