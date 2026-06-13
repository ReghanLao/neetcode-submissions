class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #basically use a stack to store operands 
        #once operator is encountered pop off two most latest elements on stack
        #and perform operation on the two 

        stack = []

        for token in tokens: 
            if token == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))

            print(stack)
        return stack[-1]