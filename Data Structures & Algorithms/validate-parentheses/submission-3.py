class Solution:
    def isValid(self, s: str) -> bool:
        maps = {')':'(', '}':'{', ']':'['}
        stack = []
        for element in s:
            if element in maps:
                if not stack or maps[element] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(element)
        return not stack