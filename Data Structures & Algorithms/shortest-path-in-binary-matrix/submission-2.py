class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        q = deque()
        q.append((0, 0))
        h = len(grid)
        w = len(grid[0])
        length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r < 0 or c < 0 or r == h or c == w or grid[r][c] == 1:
                    continue
                if r == h-1 and c == w-1 and grid[r][c] == 0:
                    return length
                grid[r][c] = 1
                for dr, dc in direction:
                    q.append((r+dr, c+dc))
            length += 1
        return -1