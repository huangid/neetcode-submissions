class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] == ".":
                    continue
                s.add(board[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] == ".":
                    continue
                s.add(board[i][j])
        for i in range(9):
            s = set()
            r = i // 3
            c = i % 3
            for j in range(9):
                r1 = j // 3
                c1 = j % 3
                if board[r*3+r1][c*3+c1] in s:
                    return False
                elif board[r*3+r1][c*3+c1] == ".":
                    continue
                s.add(board[r*3+r1][c*3+c1])
        return True
        