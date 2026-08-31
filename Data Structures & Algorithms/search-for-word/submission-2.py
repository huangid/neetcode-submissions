class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H, W = len(board), len(board[0])
        seen = set()
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r == -1 or r == H or c == -1 or c == W or board[r][c] != word[i] or (r, c) in seen:
                return False
            seen.add((r, c))
            check = backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1)
            seen.remove((r, c))
            return check
        
        for r in range(H):
            for c in range(W):
                if backtrack(r, c, 0):
                    return True
        return False