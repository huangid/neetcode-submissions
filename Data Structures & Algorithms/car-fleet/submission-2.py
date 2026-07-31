class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort(reverse=True)
        time = []
        for p, s in car:
            time.append((target-p)/s)

        stack = []
        for t in time:
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)