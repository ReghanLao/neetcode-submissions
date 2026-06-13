class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # [(]  
        for char in s:     
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                if stack:
                    if stack and char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif stack and char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif stack and char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        
        return len(stack) == 0
