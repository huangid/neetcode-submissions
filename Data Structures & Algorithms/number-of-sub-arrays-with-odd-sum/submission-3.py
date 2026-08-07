class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = 0
        odd = 0
        even = 0
        num = 0
        MOD = (10**9) + 7
        for a in arr:
            total += a
            if total % 2:
                num = (num+1+even)%MOD
                odd += 1
            else:
                num = (num+odd)%MOD
                even += 1
        return num

