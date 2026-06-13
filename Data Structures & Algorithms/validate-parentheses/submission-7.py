class Solution:
    def isValid(self, s: str) -> bool:
        #basically 
        #ensure every open bracket is closed and closed by the same type in proper order
        #every close bracket has a corresponding open bracket of same type

        #use a stack to keep track of all open brackets that need to be closed

        stack = []

        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                #ensure this close bracket has a corresponding open bracket of same type
                if stack:
                    if char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False 
                    
        return len(stack) == 0

