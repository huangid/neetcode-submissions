class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    r, c = (square // 3) * 3 + i, (square % 3) * 3 + j
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in s:
                        return False
                    s.add(board[r][c])
        return True