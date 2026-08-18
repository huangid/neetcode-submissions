class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        arr[-1] = -1
        for r in range(len(arr)-2, -1, -1):
            tmp = greatest
            if arr[r] > greatest:
                greatest = arr[r]
            arr[r] = tmp
        return arr