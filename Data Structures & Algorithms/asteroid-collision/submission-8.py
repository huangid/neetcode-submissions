class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for ast in asteroids:
            if s and ((s[-1] > 0 and ast > 0) or (s[-1] < 0 and ast < 0)):
                s.append(ast)
            elif s and s[-1] > 0 and ast < 0:
                s.append(ast)
                while len(s) >= 2 and s[-1] < 0 and s[-2] > 0:
                    if abs(s[-1]) == abs(s[-2]):
                        s.pop()
                        s.pop()
                    else:
                        if abs(s[-1]) > abs(s[-2]):
                            a = s[-1]
                            s.pop()
                            s.pop()
                            s.append(a)
                        else:
                            s.pop()
            elif s and s[-1] < 0 and ast > 0:
                s.append(ast)
            else:
                s.append(ast)
            
        return s