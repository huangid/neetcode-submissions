class Solution:
    def scoreOfString(self, s: str) -> int:
        
        i = 0
        res = 0
        for i in range(len(s)-1):
            diff = abs(ord(s[i])-ord(s[i+1]))
            res += diff
        return res