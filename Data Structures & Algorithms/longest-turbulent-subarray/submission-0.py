class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def getSize(num):
            maxSize = 1
            curSize = 1
            for r in range(len(arr)-1):
                if r % 2 == num:
                    if arr[r] > arr[r+1]:
                        curSize += 1
                    else:
                        curSize = 1
                else:
                    if arr[r] < arr[r+1]:
                        curSize += 1
                    else:
                        curSize = 1
                maxSize = max(maxSize, curSize)
            return maxSize
        return max(getSize(0), getSize(1))