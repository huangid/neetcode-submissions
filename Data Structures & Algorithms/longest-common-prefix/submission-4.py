class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        arr = list(strs[0])
        for i in range(len(arr)):
            for st in strs:
                if i >= len(st) or st[i] != arr[i]:
                    return ''.join(arr[:i])

        return ''.join(arr)