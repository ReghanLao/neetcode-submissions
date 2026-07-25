import math 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            position[i] -> position of the ith car 
            speed[i] -> speed of the ith car 

            We want to see if a car will catch up to another car or set of cars and
            form a car fleet and we want to see how many car fleets will be formed
            that arrive at destination 

            Note that the car in front will always be the bottle neck for the cars behind 
            it.

            If the car in front arrives to the destination slower than the car behind
            they become a carfleet

            If the car in front arrives faster than the car behind it they will not be a car fleet

            We only ever add a car fleet if the car in front is slower than the car behind
            Else we don't
        '''

        #create a sorted car array that stores (position, speed) and is ordered by position
        n = len(position)

        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))

        #we want to evaluate cars by the cars in front of them first as they are the
        #bottle neck so we will sort in desc order
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        
        #used to merge car fleets 
        stack = []
        print(cars)
        #for every car in car fleets we need to see when it will reach the target
        for car in cars:
            position = car[0]
            speed = car[1]
            time = (target - position) / speed

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
              
        return len(stack)
