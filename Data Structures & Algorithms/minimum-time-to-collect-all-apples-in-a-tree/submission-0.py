class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[b].append(a)
            tree[a].append(b)

        def f(cur, par):
            time = 0
            for child in tree[cur]:
                if child == par:
                    continue
                childTime = f(child, cur)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            return time
        return f(0, -1)