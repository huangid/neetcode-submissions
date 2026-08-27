class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        l = len(s)
        visit = set()
        while q:
            cur = q.popleft()
            if cur in visit:
                continue
            visit.add(cur)
            if cur == l - 1:
                return True
            nxtmin = cur + minJump
            nxtmax = min(cur + maxJump, l - 1)
            for i in range(nxtmin, nxtmax+1):
                if s[i] == '0':
                    q.append(i)
        return False