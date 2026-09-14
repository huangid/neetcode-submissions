class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        cache = {}
        visit = set()
        def search(i, j, k):
            if k == len(word):
                return True
            if i == -1 or i == h or j == -1 or j == w:
                return False
            if (i, j) in visit or board[i][j] != word[k]:
                return False
            visit.add((i, j))
            ans = False
            ans = search(i-1, j, k+1) or search(i+1, j, k+1) or search(i, j-1, k+1) or search(i, j+1, k+1)
            visit.remove((i, j))
            return ans
        
        for i in range(h):
            for j in range(w):
                if search(i, j, 0):
                    return True
        return False