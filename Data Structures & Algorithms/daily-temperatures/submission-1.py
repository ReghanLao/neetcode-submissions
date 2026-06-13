class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #basically we use a stack to keep track of the temperatures that we 
        #encounter and want to find warmer temperatures for

        #once we do find a watmer temp thru traversing the temps array
        #go ahead and pop off the less warmer temp from stack and calc the number of days it takes to appear

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            #if and only if there is/are temperatures to be resolve then can we resolve them
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days = i - stack[-1]
                res[stack[-1]] = days 
                stack.pop()
                
            stack.append(i)
                
        return res 