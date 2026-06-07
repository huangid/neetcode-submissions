class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            sortedS = "".join(sorted(string))

            map[sortedS].append(string)

        return list(map.values())