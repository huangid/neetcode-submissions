class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = list()
        length = 0
        for i, char in enumerate(s):
            while char in lst:
                lst.pop(0)
            lst.append(char)
            length = max(length, len(lst))
        return length