class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = { ")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in bracket_pairs:
                if len(stack) > 0 and stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0 
