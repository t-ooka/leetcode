class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>num_set(nums.begin(), nums.end());
        int longest = 0;

        for (auto &n: num_set) {
            if (!num_set.contains(n-1)) {
                int length = 1;
                while (num_set.contains(n + length)) {
                    length += 1;
                }
                longest = max(length, longest);
            }
        }

        return longest;
    }
};
