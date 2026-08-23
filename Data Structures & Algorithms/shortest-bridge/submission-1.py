class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != 1:
                return
            grid[i][j] = 2          # mark as part of island #1
            q.append((i, j))        # seed for multi-source BFS
            for di, dj in dirs:
                dfs(i + di, j + dj)

        # Step 1: flood-fill the first island
        found = False
        for i in range(h):
            if found:
                break
            for j in range(w):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # Step 2: multi-source BFS expanding level by level
        steps = 0
        while q:
            for _ in range(len(q)):          # process one full level
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w:
                        if grid[nr][nc] == 1:   # reached island #2
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2    # mark visited water
                            q.append((nr, nc))
            steps += 1
        return -1
