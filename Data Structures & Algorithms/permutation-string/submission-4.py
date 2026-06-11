class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(s1)
        l = len(s1)
        for i in range(len(s2) - len(s1) + 1):
            if s == sorted(s2[i:i+l]):
                return True
        return False