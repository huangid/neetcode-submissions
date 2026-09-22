class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))
        
        i = 0
        res = []
        for i, c in enumerate(s):
            if (c, i) not in stack:
                res.append(c)
        return "".join(res)
