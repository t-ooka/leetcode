class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        freq_num_pairs = [(cnt, num) for num, cnt in counts.items()]
        freq_num_pairs.sort(reverse=True)
        result = [num for _, num in freq_num_pairs[:k]]
        return result
