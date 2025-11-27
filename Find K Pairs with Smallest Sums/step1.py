class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        list_of_pairs = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                list_of_pairs.append((nums1[i], nums2[j]))
        sorted_list_of_pairs = sorted(list_of_pairs, key=lambda x: sum(x))
        return sorted_list_of_pairs[:k]
