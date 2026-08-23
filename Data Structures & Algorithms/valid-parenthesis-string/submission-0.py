class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == ')':
                if not left and not star:
                    return False
                elif left:
                    left.pop()
                else:
                    star.pop()
            else:
                star.append(i)
        while star and left:
            if star[-1] > left[-1]:
                star.pop()
                left.pop()
            else:
                return False
        return not left