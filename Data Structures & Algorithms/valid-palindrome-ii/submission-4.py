class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        jump = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if not jump:
                    return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
                else:
                    return False

        return True