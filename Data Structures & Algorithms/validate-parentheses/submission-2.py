class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        open_ = ['(', '[', '{']
        closed_ = [')', ']', '}']
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in open_:
                stack.append(char)
            
            elif char in closed_:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        