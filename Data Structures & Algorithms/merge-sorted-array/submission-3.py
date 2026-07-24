class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        for l in range(m+n-1, -1, -1):
            if i1 >= 0 and i2 >= 0:
                if nums1[i1] > nums2[i2]:
                    nums1[l] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[l] = nums2[i2]
                    i2 -= 1
                
            elif i1 >= 0:
                nums1[l] = nums1[i1]
                i1 -= 1
            else:
                nums1[l] = nums2[i2]
                i2 -= 1
