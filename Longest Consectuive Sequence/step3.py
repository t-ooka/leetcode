class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest_consecutive_sequence = 1

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest_consecutive_sequence = max(length, longest_consecutive_sequence)

        return longest_consecutive_sequence
