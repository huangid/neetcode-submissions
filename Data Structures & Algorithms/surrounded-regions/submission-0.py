class Solution:
    def solve(self, board: List[List[str]]) -> None:
        h, w = len(board), len(board[0])
        def surround(r, c):
            if r < 0 or r == h or c < 0 or c == w or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'
            surround(r+1, c)
            surround(r-1, c)
            surround(r, c+1)
            surround(r, c-1)
        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    if board[i][j] == 'O':
                        surround(i, j)
        for i in range(h):
            for j in range(w):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        