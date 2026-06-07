class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            sortedS = "".join(sorted(string))
            if sortedS not in map:
                map[sortedS] = []
            map[sortedS].append(string)

        return list(map.values())