class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        group = []

        for string in strs:
            sort = "".join(sorted(string))
            if sort in map:
                map[sort].append(string)
            else:
                map[sort] = []
                map[sort].append(string)

        for value in map.values():
            group.append(value)

        return group