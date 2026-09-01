class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        frequency_num_pairs = []
        for key, cnt in counts.items():
            frequency_num_pairs.append((cnt, key))
        frequency_num_pairs.sort(reverse=True)
        return [num for _, num in frequency_num_pairs[:k]]
