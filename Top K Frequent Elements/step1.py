class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_counts = {}

        for num in nums:
            int_counts[num] = int_counts.get(num, 0) + 1

        sorted_int_coutns = sorted(int_counts.items())
