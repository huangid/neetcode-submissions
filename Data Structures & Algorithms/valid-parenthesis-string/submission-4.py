class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while left and star:
            if left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return not left