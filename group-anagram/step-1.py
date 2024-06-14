class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for s in strs:
            arr = [0] * 26
            for l in s:
                arr[ord(l) - 97] += 1
            ans.get(tuple(arr), []).append(s)
        return ans.values()
