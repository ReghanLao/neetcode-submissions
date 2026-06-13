class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #pair heaviest + least heaviest to be efficient in creating the 
        #minimum of boats required to store everyone 

        people.sort()
        boats = 0 

        left = 0 
        right = len(people) - 1
        print(people)
        while left <= right:   

            #if there is only one person remaining place them into a boat by themselves
            if left == right:
                boats += 1
                left += 1
                right -= 1
                break

            #try pair people at left and right 
            if people[left] + people[right] <= limit:
                #if their weights are less than the limit we can put them into one boat
                boats += 1
                print(left, right)
                left += 1
                right -= 1
            else:
                #else the weights of both individuals are greater than the limit
                #place the heavier individual in the boat to continue being 
                #efficient in creating weight pairs later on 
                print(right)
                boats += 1
                right -= 1
        
        return boats
