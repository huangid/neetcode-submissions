class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in m:
                if stack and stack[-1] == m[char]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(char)

        return not stack