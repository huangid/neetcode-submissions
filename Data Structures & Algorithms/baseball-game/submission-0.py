class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for s in operations:
            if s == '+':
                record.append(record[-1]+record[-2])
            elif s == 'D':
                record.append(2*record[-1])
            elif s == 'C':
                record.pop()
            else:
                record.append(int(s))

        return sum(record)