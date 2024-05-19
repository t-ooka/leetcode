class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freqcount = defaultdict(int) 

        for num in nums:
            num_to_freqcount[num] = num_to_freqcount[num] + 1

        same_freq_counts = [[] for i in range(len(nums)+1)]

        for key, value in num_to_freqcount.items():
            same_freq_counts[value].append(key)
        
        return sum(reversed(same_freq_counts), [])[:k]
