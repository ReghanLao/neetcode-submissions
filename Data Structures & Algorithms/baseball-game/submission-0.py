class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        n = len(operations)

        for i in range(n):
            if operations[i] == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif operations[i] == 'D':
                stack.append(int(stack[-1]) * 2)
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)
