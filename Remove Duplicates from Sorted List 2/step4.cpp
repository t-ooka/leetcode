/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

int INITIAL_VALUE = -1000;

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
      ListNode* dummy = new ListNode(INITIAL_VALUE, head);
      ListNode* previous_node = dummy;
      ListNode* current_node = head;

      while (current_node) {
        while (current_node->next && current_node->val == current_node->next->val) {
          current_node = current_node->next;
        }
        if (previous_node->next == current_node) {
          previous_node = previous_node->next;
        } else {
          previous_node->next = current_node->next;
        }
        current_node = current_node->next;
      }
      return dummy->next;
        
    }
};
