class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        l = len(s)
        far = 0
        while q:
            cur = q.popleft()
            if cur == l - 1:
                return True
            nxtmin = max(far + 1, cur + minJump)
            nxtmax = min(cur + maxJump, l - 1)
            for i in range(nxtmin, nxtmax+1):
                if s[i] == '0':
                    q.append(i)
            far = nxtmax
        return False