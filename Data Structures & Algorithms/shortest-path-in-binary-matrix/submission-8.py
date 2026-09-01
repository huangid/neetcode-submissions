class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        h, w = len(grid), len(grid[0])
        direct = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        q = deque()
        q.append((0, 0))
        path = 1
        if h == 1 and w == 1:
            return 1
        while q:
            path += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    if row == h - 1 and col == w - 1:
                        return path
                    if 0 <= row < h and 0 <= col < w and grid[row][col] == 0:
                        grid[row][col] = 1
                        q.append((row, col))
        return -1
        