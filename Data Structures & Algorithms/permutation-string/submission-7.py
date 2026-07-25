class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for i in range(len(s2)-len(s1)+1):
            if s2[i] not in s1:
                continue
            c1 = Counter(s1)
            for j in range(i, i+len(s1)):
                if s2[j] in s1:
                    c1[s2[j]] -= 1
            if all(v == 0 for v in c1.values()):
                return True
                
        return False