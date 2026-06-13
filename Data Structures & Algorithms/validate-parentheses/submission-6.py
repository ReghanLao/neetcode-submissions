class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s: 
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    #that means we have a potential corresponding
                    #opening brace for the current close brace 
                    #we can check the top of the stack
                    #if they are of the same type
                    #a stack allows to keep track of this idea
                    #of brackets closing in the right order
                    if char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False 

        return len(stack) == 0