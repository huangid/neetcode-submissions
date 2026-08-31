class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direct = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        h, w = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append((0, 0))
        path = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == h - 1 and c == w - 1:
                    return path
                grid[r][c] = 1
                for dr, dc in direct:
                    if -1 < r + dr < h and -1 < c + dc < w and grid[r+dr][c+dc] == 0:
                        q.append((r+dr, c+dc))
            path += 1
        return -1