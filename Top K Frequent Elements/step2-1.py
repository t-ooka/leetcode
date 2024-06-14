class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        num_freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_hash[num] = count_hash.get(num, 0) + 1
        
        for key, value in count_hash.items():
            num_freq[value].append(key)
        
        ans = []
        for i in range(len(num_freq)-1, 0, -1):
            for ele in num_freq[i]:
                ans.append(ele)
                if len(ans) == k:
                    return ans 
        
