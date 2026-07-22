class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(sum(row[col1:col2+1]) for row in self.m[row1:row2+1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)