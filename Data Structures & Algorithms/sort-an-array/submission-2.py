class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        def find(arr, num):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        for i, num in enumerate(nums):
            index = find(ans, num)
            ans.insert(index, num)
        return ans
        
