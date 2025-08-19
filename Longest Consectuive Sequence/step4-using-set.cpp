class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set nums_set(nums.begin(), nums.end());
        int longest_consecutive_sequence = 0;

        for ( auto num: nums_set) {
            if ( !nums_set.contains(num - 1)) {
                int length = 1;
                while (nums_set.contains(num + length)) {
                    length++;
                }
                longest_consecutive_sequence = max(length, longest_consecutive_sequence);
            }
        }

        return longest_consecutive_sequence;
    }
};
