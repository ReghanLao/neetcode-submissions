class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x: x[0])

        stack = []
        for pos, speed in reversed(cars):
            if stack:
                behind_arrival_time = (target - pos) / speed
                front_arrival_time = (target - stack[-1][0]) / stack[-1][1]

                if front_arrival_time < behind_arrival_time:
                    #seperate fleet forms behind because this car cannot catch up
                    stack.append((pos, speed))
            else:
                stack.append((pos, speed))
        
        return len(stack)