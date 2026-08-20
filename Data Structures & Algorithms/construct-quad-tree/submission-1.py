"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        h = len(grid)
        w = len(grid[0])
        first = grid[0][0]
        if all(grid[i][j] == first for i in range(h) for j in range(w)):
            return Node(val=bool(first), isLeaf=True)
        isLeaf = False
        halfH = h // 2
        halfW = w // 2
        topLeft = self.construct([row[:halfW] for row in grid[:halfH]])
        topRight = self.construct([row[halfW:] for row in grid[:halfH]])
        bottomLeft = self.construct([row[:halfW] for row in grid[halfH:]])
        bottomRight = self.construct([row[halfW:] for row in grid[halfH:]])
        return Node(False, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
