class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = r = 0
        q = deque()
        q.append(0)
        while q:
            i = q.popleft()
            l = max(r + 1, i + minJump)
            r = min(i + maxJump, len(s) - 1)
            for j in range(l, r+1):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    q.append(j)
        return False
