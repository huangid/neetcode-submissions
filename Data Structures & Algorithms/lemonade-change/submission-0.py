class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0] * 2 # 5, 10
        for i, bill in enumerate(bills):
            if bill == 5:
                arr[0] += 1
            elif bill == 10:
                if arr[0] == 0:
                    return False
                arr[0] -= 1
                arr[1] += 1
            elif bill == 20:
                if arr[1] >= 1 and arr[0] >= 1:
                    arr[1] -= 1
                    arr[0] -= 1
                elif arr[0] >= 3:
                    arr[0] -= 3
                else:
                    return False
        return True
