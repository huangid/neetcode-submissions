class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                r = stack.pop()
                l = stack.pop()
                if c == "+":
                    stack.append(l+r)
                elif c == "-":
                    stack.append(l-r)
                elif c == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))
            else:
                stack.append(int(c))
        return stack[-1]