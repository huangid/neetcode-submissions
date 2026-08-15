class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            sort = ''.join(sorted(s))
            m[sort].append(s)
        return list(m.values())
