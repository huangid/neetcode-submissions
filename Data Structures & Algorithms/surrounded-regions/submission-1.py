class Solution:
    def solve(self, board: List[List[str]]) -> None:
        h, w = len(board), len(board[0])
        def dfs(i, j):
            if i == -1 or i == h or j == -1 or j == w or board[i][j] == '#' or board[i][j] == 'X':
                return
            board[i][j] = '#'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    if board[i][j] == 'O':
                        dfs(i, j)
        for i in range(h):
            for j in range(w):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
