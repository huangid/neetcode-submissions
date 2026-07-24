class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 1
        n = len(nums)
        st = set()
        st.add(nums[0])
        for i in range(1, n):
            if nums[i] in st:
                continue
            else:
                nums[k] = nums[i]
                st.add(nums[k])
                k += 1
        return k