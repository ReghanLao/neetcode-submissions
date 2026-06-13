class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        position_speed_pairs = []

        for pos, speed in zip(position, speed):
            position_speed_pairs.append((pos,speed))
        
        sorted_position_speed_pairs = sorted(position_speed_pairs)

        for pos, speed in reversed(sorted_position_speed_pairs):
            speed = (target - pos) / speed
            stack.append(speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #now that have adjacent cars does the car
                #that we just added going to collide with the one
                #in front of it?
                #yes then we remove this car from its own fleet
                #and we add it to the existing fleet of the car in front
                stack.pop()

        return len(stack)

