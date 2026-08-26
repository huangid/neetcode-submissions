class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i, par):
            if not adj[i]:
                return 1
            height = 0
            for child in adj[i]:
                if child == par:
                    continue
                height = max(height, dfs(child, i))
            return height + 1
        heightArr = []
        for i in range(n):
            heightArr.append((dfs(i, -1), i))
        
        heightArr.sort()
        minH = heightArr[0][0]
        return [i for h, i in heightArr if h == minH]
            