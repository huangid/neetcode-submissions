class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c:i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            a, b = words[i], words[i+1]
            for j in range(len(a)):
                if j == len(b):
                    return False
                if a[j] != b[j]:
                    if m[a[j]] > m[b[j]]:
                        return False
                    break

        return True