class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        H = len(grid)
        W = len(grid[0])
        fresh = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        time = 0
        while q and fresh:
            for n in range(len(q)):
                x, y = q.popleft()
                for dx, dy in direction:
                    if 0 <= x + dx < H and 0 <= y + dy < W and grid[x+dx][y+dy] == 1:
                        q.append([x+dx, y+dy])
                        grid[x+dx][y+dy] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1