class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        H, W = len(grid), len(grid[0])
        visit = set()
        q = deque()
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))

        def addRoom(x, y):
            if x == -1 or x == H or y == -1 or y == W or (x, y) in visit or grid[x][y] == -1:
                return
            q.append([x, y])
            visit.add((x, y))

        dist = 0
        while q:
            for n in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist
                addRoom(x+1, y)
                addRoom(x-1, y)
                addRoom(x, y+1)
                addRoom(x, y-1)
            dist += 1
