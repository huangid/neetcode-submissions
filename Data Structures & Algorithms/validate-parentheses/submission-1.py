class Solution:
    def isValid(self, s: str) -> bool:
        maps = {')':'(', '}':'{', ']':'['}
        stack = []
        for element in s:
            if element in maps and stack and maps[element] == stack[-1]:
                stack.pop()
            else:
                stack.append(element)
        return not stack