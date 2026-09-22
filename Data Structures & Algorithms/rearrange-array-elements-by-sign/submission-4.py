class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = True
        p1 = 0
        p2 = 0
        res = []
        while len(res) != len(nums):
            if pos:
                while nums[p1] < 0:
                    p1 += 1
                res.append(nums[p1])
                p1 += 1
            else:
                while nums[p2] > 0:
                    p2 += 1
                res.append(nums[p2])
                p2 += 1
            pos = not pos
        return res