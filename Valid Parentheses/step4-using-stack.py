class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_to_closing = { "(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in opening_to_closing:
                stack.append(opening_to_closing[bracket])
                continue
            else:
                if not stack or bracket != stack.pop():
                    return False
        return not stack
