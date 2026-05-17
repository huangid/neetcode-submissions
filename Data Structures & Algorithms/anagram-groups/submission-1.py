class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            sortS = "".join(sorted(string))
            if sortS not in map:
                map[sortS] = []
            map[sortS].append(string)

        return list(map.values())