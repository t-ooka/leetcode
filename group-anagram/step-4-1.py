# Using dict for counting the number of characters

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            char_count = {}
            for l in s:
                if l not in char_count:
                    char_count[l] = 1
                else:
                    char_count[l] += 1
            key = tuple(sorted(char_count.items()))
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)
            
        return ans.values()
