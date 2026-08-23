class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [False] * 3
        for tri in triplets:
            if tri[0] <= target[0] and tri[1] <= target[1] and tri[2] <= target[2]:
                for i in range(3):
                    if tri[i] == target[i]:
                        check[i] = True
        return all(c == True for c in check)