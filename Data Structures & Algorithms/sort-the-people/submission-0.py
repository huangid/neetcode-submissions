class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m = {}
        for name, h in zip(names, heights):
            m[h] = [h, name]
        
        heights.sort()
        res = []
        for hei in heights:
            res.append(m[hei][1])

        return res[::-1]
        