class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000", 0))
        visit = set(deadends)
        def child(lock):
            res = []
            for i in range(4):
                c = str((int(lock[i]) + 1) % 10)
                lock1 = lock[:i] + c + lock[i+1:]
                res.append(lock1)
                c = str((int(lock[i]) - 1 + 10) % 10)
                lock2 = lock[:i] + c + lock[i+1:]
                res.append(lock2)
            return res
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            for c in child(lock):
                if c not in visit:
                    visit.add(c)
                    q.append((c, turn + 1))
        return -1