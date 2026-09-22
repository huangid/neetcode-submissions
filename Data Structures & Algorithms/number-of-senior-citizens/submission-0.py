class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                n += 1

        return n
