class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        m = Counter(hand)
        while m:
            val = min(list(m.keys()))
            for _ in range(groupSize):
                if val not in m:
                    return False
                m[val] -= 1
                if m[val] == 0:
                    del m[val]
                val += 1
        return True

