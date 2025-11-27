class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_size, nums2_size = len(nums1), len(nums2)
        if nums1_size == 0 or nums2_size == 0 or k == 0: # 今回の条件では不要
            return []
        
        result = []
        heap = []

        for i in range(min(k, nums1_size)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while heap and len(result) < k:
            summation, num1, num2 = heapq.heappop(heap)
            result.append([nums1[num1], nums2[num2]])

            if num2 + 1 < nums2_size:
                heapq.heappush(heap, (nums1[num1] + nums2[num2 + 1], num1, num2 + 1))
        
        return result

        
