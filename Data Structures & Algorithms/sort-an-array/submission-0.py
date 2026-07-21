class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            temp = []
            while ans and ans[-1] > num:
                temp.append(ans.pop())
            ans.append(num)
            temp.reverse()
            ans.extend(temp)
        return ans