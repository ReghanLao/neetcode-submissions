class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                unresolved_day = stack.pop()
                days = i - unresolved_day
                result[unresolved_day] = days
            
            stack.append(i)

        return result 
