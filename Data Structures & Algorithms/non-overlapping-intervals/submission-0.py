class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        count = 0
        for s, e in intervals:
            if res and s < res[-1][1]:
                count += 1
                s1, e1 = res.pop()
                newS = s if e < e1 else s1
                newE = e if e < e1 else e1
                res.append([newS, newE])
            else:
                res.append([s, e])
        return count