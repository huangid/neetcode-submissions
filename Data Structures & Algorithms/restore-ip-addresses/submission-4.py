class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        res = []
        def dfs(i):
            if i == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) == 4 or i == len(s):
                return
            path.append(s[i])
            dfs(i+1)
            path.pop()
            if s[i] in '123456789':
                if i + 1 < len(s):
                    path.append(s[i:i+2])
                    dfs(i+2)
                    path.pop()
            if s[i] == '1':
                if i + 2 < len(s):
                    path.append(s[i:i+3])
                    dfs(i+3)
                    path.pop()
            elif s[i] == '2':
                if i + 2 < len(s) and int(s[i:i+3]) <= 255:
                    path.append(s[i:i+3])
                    dfs(i+3)
                    path.pop()
        dfs(0)
        return res
            