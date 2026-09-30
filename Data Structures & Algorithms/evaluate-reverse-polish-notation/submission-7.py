import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }

        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                result = math.trunc(operators[token](a, b))
                stack.append(result)
            else:
                stack.append(token)
        return int(stack[0])