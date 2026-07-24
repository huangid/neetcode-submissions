class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if l == r:
                num += 1
                return num
            if people[l] + people[r] > limit:
                r -= 1
                num += 1
            else:
                r -= 1
                l += 1
                num += 1
        return num
