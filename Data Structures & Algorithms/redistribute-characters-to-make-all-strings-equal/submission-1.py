class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = defaultdict(int)
        for w in words:
            for c in w:
                cnt[c] += 1

        for f in cnt.values():
            if f % len(words) != 0:
                return False
        return True