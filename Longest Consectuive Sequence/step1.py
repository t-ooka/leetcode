class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_to_index = {}

        for i in range(0, len(nums)):
            num_to_index[nums[i]] = i
        
        longest_sequence = 1

        for key in num_to_index.keys():
            count = 1
            while key+1 in num_to_index:
                count += 1
                key += 1
            
            longest_sequence = max(count, longest_sequence)
        
        return longest_sequence
        
