class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = {}
        frequency_to_nums = [ [] for i in range(len(nums) + 1)]

        for num in nums:
            num_to_frequency[num] = 1 + num_to_frequency.get(num, 0)
        for num, frequency in num_to_frequency.items():
            frequency_to_nums[frequency].append(num)
        
        res = []
        for i in range(len(frequency_to_nums) - 1, 0, -1):
            for num in frequency_to_nums[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
