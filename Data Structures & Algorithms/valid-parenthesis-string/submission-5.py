class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif c == '(':
                left.append(i)
            else:
                star.append(i)
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return not left