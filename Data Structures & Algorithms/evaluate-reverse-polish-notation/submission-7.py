class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                r = int(stack.pop())
                l = int(stack.pop())
                if c == "+":
                    stack.append(l+r)
                elif c == "-":
                    stack.append(l-r)
                elif c == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))
            else:
                stack.append(c)
        return int(stack[-1])