class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        m = {}
        if len(arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]] = arr[i]
            if m[pattern[i]] != arr[i]:
                return False
        
        if len(set(m.values())) != len(m):
            return False
        return True
            