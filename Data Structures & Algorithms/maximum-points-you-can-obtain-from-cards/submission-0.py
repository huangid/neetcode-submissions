class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        total = sum(cardPoints)
        l = 0
        curSum = sum(cardPoints[:n])
        minSum = curSum
        for r in range(n, len(cardPoints)):
            curSum -= cardPoints[l]
            l += 1
            curSum += cardPoints[r]
            minSum = min(curSum, minSum)
        return total - minSum