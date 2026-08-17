class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        def dfs(i, j, org):
            if i < 0 or j < 0 or i == h or j == w or image[i][j] != org or image[i][j] == color:
                return
            
            image[i][j] = color
            dfs(i+1, j, org)
            dfs(i-1, j, org)
            dfs(i, j+1, org)
            dfs(i, j-1, org)

        dfs(sr, sc, image[sr][sc])
        return image