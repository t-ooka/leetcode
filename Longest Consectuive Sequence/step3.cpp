class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.rbegin(), nums.rend());
        int longest_consecutive_sequence = 0;

        for ( auto &n: nums) {
            if (!num_set.contains(n-1)) {
                int length = 1;
                while (num_set.contains(n + length)) {
                    length += 1;
                }
                longest_consecutive_sequence = max(length, longest_consecutive_sequence);
            }
        }
        return longest_consecutive_sequence;
    }
};
