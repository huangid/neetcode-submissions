class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        st = ""
        n = 0
        for c in s:
            if c.isdigit():
                n = n*10 + int(c)
            elif c == '[':
                stack.append((st, n))
                st, n = "", 0
            elif c == ']':
                ps, pn = stack.pop()
                st = ps + st*pn
            else:
                st += c
        
        return st
