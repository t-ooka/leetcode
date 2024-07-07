class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        count = {}
        word_freq = [[] for i in range(len(nums) + 1)]
        ans = []
       
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            word_freq[value].append(key)
        
        for i in range(len(word_freq)-1, -1, -1):
            for ele in word_freq[i]:
                ans.append(ele)
                if k == len(ans):
                    return ans
