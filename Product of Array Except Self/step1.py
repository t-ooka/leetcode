class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]+prefix[])
