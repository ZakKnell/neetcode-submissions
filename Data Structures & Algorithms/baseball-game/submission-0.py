class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                l = len(stack)
                stack.append(stack[l - 1] + stack[l - 2])
            elif operation == 'D':
                stack.append(2* stack[-1])
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        answer = 0
        for num in stack:
            answer = answer + num
        
        return answer