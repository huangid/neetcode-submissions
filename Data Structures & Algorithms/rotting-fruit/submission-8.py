class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        h, w = len(grid), len(grid[0])
        fresh = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        time = 0
        while fresh and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    i, j = r + dr, c + dc
                    if -1 < i < h and -1 < j < w and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        q.append((i, j))
            time += 1
        return time if fresh == 0 else -1
                    