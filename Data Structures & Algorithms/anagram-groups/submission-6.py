class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in m:
                m[sort].append(s)
            else:
                m[sort] = []
                m[sort].append(s)
        return list(m.values())
