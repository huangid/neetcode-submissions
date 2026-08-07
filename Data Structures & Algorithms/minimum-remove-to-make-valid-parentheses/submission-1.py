class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        arr = list(s)
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
            elif c == ')' and cnt > 0:
                cnt -= 1
            elif c == ')':
                arr[i] = ''
        res = []
        for c in reversed(arr):
            if c == '(' and cnt > 0:
                cnt -= 1
            else:
                res.append(c)

        return ''.join(res[::-1])
                