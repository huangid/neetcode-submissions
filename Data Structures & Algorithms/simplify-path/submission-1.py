class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for p in arr:
            if p == '..':
                if stack:
                    stack.pop()
            elif p != '' and p != '.':
                stack.append(p)

        return "/" + "/".join(stack)