class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #rules naturally follow the notion of a sliding window 
        #we want a fixed sized hashmap of size 2 to keep track of the current fruits in our buckets 
        #if the size of our hashmap exceeds 2 then we want to remove the element at the front of the window and slide the window over to include the new element
        #this is simulating our baskets only holding 2 types of fruits and the moment we include a new type we must remove an old type from consideration to 
        #continously calculate the max number of fruits we can pick 

        max_fruits = float('-inf')
        curr_fruits = 0 
        buckets = {}

        #the start of the window (left and right define the bounds of the fruits we are currently considering filling our buckets with)
        left = 0 
        
        for right in range(len(fruits)):
            fruit_type = fruits[right]
            buckets[fruit_type] = buckets.get(fruit_type, 0) + 1
            curr_fruits += 1
            print(curr_fruits)
            while len(buckets) > 2:
                curr_fruits -= 1
                buckets[fruits[left]] -= 1
                if buckets[fruits[left]] == 0:
                    buckets.pop(fruits[left])
                left += 1
            
            max_fruits = max(max_fruits, curr_fruits)
        
        return max_fruits 


