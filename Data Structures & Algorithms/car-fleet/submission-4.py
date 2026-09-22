class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for p, s in zip(position, speed):
            arr.append([p, s])
        arr.sort(reverse=True)
        stack = []
        for p, s in arr:
            t = (target-p)/s
            if not stack:
                stack.append(t)
            elif stack[-1] < t:
                stack.append(t)
        
        return len(stack)