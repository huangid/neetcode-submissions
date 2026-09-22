class Solution:
    def isValid(self, s: str) -> bool:
        MAP = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in MAP:
                if stack and MAP[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        