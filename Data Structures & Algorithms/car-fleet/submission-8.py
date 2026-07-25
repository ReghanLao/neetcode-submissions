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


        '''
        Takeaways:
        1. Ask "what needs to be known before I can decide about this item?"
        and let that dictate direction, rather than defaulting 
        to sorting/iterating in whatever order feels natural 
        (usually ascending/left-to-right).

        2. Your first version tried to compare stack[-2] vs stack[-1]
        and repair things by popping/re-pushing. Once the iteration order is correct, you never need to look further than stack[-1] — that's the signature of a well-formed monotonic stack pattern. If you find yourself reaching deeper into the stack or 
        rewriting values that are already there, 
        it's usually a sign the direction or invariant is off,
         not that you need fancier stack surgery.

        3. DONT ASSUME that we need to round calculations to the nearest upper int
        if that is not stated

        4. f two conditions are meant to be mutually exclusive, make that explicit with elif.
        '''
