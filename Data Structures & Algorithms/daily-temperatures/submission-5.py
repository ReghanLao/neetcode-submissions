class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            Brute Force: 
            The most intuitive brute force solution would require us to check for every day
            what is the next day in which a warmer temperature would appear in the future

            Aka for every temperature in the array when is the next warmer temperature appearing - this worst case iterates through n temperatures and for every temperature n - 1 temperatures in the worst case are checked to see when that warmer temperature appears 

            This runs in n^2 time worst case which is not very efficient 

            More efficient: 
            A better solution would be to constantly keep track of the temperatures we have seen in a data strcture like a stack.
            
            Why a stack? 
            
            Well a stack allows us to have insight and access to the most recent temperature(s) we come across which is relevant to seeing when a new warmer tempearture comes in and specifically how many days in the future this warmer temperature comes in at 

            If we know the temperatures that we iterate through and have access to them, the moment a new warmer tempearture beats these amount of temperatures on the stack we know how many days in the future a warmer temp appears for all these temperatures potentially on the stack.

            Basically we need access to the temperatures we recently iterate over and be able to tell & calculate when a warmer temp appears and a stack helps us persist that memory 
        '''

        res = [0] * len(temperatures)

        #we will store indicies on the stack to make day calculations easier and day's in the future assignments easier in the res array
        stack = []

        for i in range(len(temperatures)):

            #a warmer temperature has occured at i for a day in the past noted in stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                past_day = stack.pop()

                #a warmer temperature for the past day occurs in i - past_day days 
                res[past_day] = i - past_day

            #after we have resolved all applicable past days for when the temp thats about to be added to greater than these past days we can add this temp's index to the stack - stack therefore is a monotonically decreasing stack
            stack.append(i)

        
        return res 
