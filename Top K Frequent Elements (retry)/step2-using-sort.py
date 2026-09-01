class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = {}
        for num in nums:
            num_to_frequency[num] = 1 + num_to_frequency.get(num, 1)
        
        frequency_to_num_array = []
        for num, frequency in num_to_frequency.items():
            frequency_to_num_array.append([frequency, num])
        frequency_to_num_array.sort()

        res = []
        while len(res) < k:
            res.append(frequency_to_num_array.pop()[1])
        return res
      
        
