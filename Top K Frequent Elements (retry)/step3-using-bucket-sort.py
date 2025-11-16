class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency_buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, cnt in counts.items():
            frequency_buckets[cnt].append(num)
        result = []
        for frequency_value in range(len(frequency_buckets) - 1, 0, -1):
            for num in frequency_buckets[frequency_value]:
                result.append(num)
                if len(result) == k:
                    return result
