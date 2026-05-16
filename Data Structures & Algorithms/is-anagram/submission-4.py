class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = Counter()
        th = Counter()

        if (len(s) != len(t)):
            return False

        for s1, t1 in zip(s, t):
            if s1 not in sh:
                sh[s1] = 1
            else:
                sh[s1] += 1
            if t1 not in th:
                th[t1] = 1
            else:
                th[t1] += 1


        return sh == th