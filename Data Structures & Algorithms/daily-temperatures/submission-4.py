class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Intuitive brute force approach is to check for every 
            temperature when a future warmer temperature will appear 

            res = [0] * len(temperatures)

            for i in range(len(temperatures)):
                day_count = 0
                for j in range(i + 1, len(temperatures)):
                    day_count += 1 
                    if temperatures[j] > temperatures[i]:
                        res[i] = day_count
                        break 
            
            return res     

            But this is an O(n^2) solution

            We can sacrifice space for speed and utilize a stack for this problem
            
            Since we are concerned with future temperatures we can simply 
            add temperatures to the stack as we go and if the temperature we
            are about to add is greater than the temperature on top of the stack
            aka the temperature in the past we can pop that past temperature off the 
            stack and calculate the pop count aka the number of days that warmer temp
            appears after that past temp

            The reason why a stack fits so well is because we always want to be able
            to compare the most recent temp on the stack with the about to be added temp.

            If that most recent temp on the stack is lower we have found a warmer temp
            in the future in x days aka x pops from the stack 
        '''

        #since we need reference to the index (for result setting) and the temp
        #we will store (index, temp) tuples 
        stack = []

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            days = 0
            #outer if handles initial case of adding first temp
            if stack:
                #once we actual have temps we can begin the calculating of days in the
                #future that a warmer temp will occur for a given index 
                while stack and stack[-1][1] < temperatures[i]:
                    recent_index, _ = stack.pop()
                    days = i - recent_index
                    res[recent_index] = days    

                stack.append((i, temperatures[i])) 
            else:
                stack.append((i, temperatures[i])) 
        
        return res
        