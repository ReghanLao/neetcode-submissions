class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Intuitive brute force approach is to check for every 
            temperature when a future warmer temperature will appear 

            But this is an O(n^2) solution
        '''
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            day_count = 0
            for j in range(i + 1, len(temperatures)):
                day_count += 1 
                if temperatures[j] > temperatures[i]:
                    res[i] = day_count
                    break 
        
        return res 