class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            To represent the notion that car cannot pass another car
            in front of it and it has to join the car fleet in front of it 
            
            we can use a stack to keep track of the car fleets and its
            time to hit destination - we need a convenient way to access 
            that most recent aka the car in the front of us's time to destination
            and we 
            only add to this stack if we find that a car is unable to catch
            up to a car fleet in front of it, leaving us with the total number
            of car fleets left on this stack/list 

            A car joins a car fleet if it is able to reach the destination at the 
            same time as the car fleet in front of it or if its able to pass the 
            car fleet in front of it 

            when we are evaluating whether to form a new car fleet or not
            we have to know when the car fleet in front finishes

            so we need to evaluate our cars sorted by desc position because the cars
            in front of other cars will always be the bottleneck that lets us know
            whether or not we need to form new car fleets or not 
        '''

        #car will be defined as a (position, speed) tuple
        cars = []

        #represents the distinct car fleets 
        stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars = sorted(cars, key=lambda item: item[0], reverse=True)

        for car in cars:
            #calculate it takes for car X to get to destination
            car_pos = car[0]
            car_speed = car[1]

            time = (target - car_pos) / car_speed 

            #if there's no car fleet yet add to the stack
            if not stack:
                stack.append(time)
            #if there is a car fleet on the stack check if the car fleet on the stack
            #aka the car fleet in front of it is faster than this car X's arrival time
            #to destination and if so well a new car fleet is formed 
            elif time > stack[-1]:
                stack.append(time)
            #the car X joins carfleet in front of it since its already defined on the stack
            #no need to add it again
            else:
                pass
                
        return len(stack)



