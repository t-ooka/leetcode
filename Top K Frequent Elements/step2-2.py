class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        return heapq.nlargest(k, count.keys(), key=count.get)
