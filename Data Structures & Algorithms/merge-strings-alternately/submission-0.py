class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        l2 = 0
        merge = []
        while l1 < len(word1) and l2 < len(word2):
            merge.append(word1[l1])
            l1 += 1
            merge.append(word2[l2])
            l2 += 1

        if l1 < len(word1):
            merge.extend(word1[l1:])
        if l2 < len(word2):
            merge.extend(word2[l2:])
        return "".join(merge)