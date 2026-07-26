# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        res = (l+r) // 2
        while guess(res) != 0:
            if guess(res) == -1:
                r = res - 1
            elif guess(res) == 1:
                l = res + 1
            res = (l+r) // 2
        return res
        