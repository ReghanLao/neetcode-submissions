class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #rules naturally follow the notion of a sliding window 
        #we want a fixed sized hashmap of size 2 to keep track of the current fruits in our buckets 
        #if the size of our hashmap exceeds 2 then we want to remove the element at the front of the window until we have an open bucket again and slide the window over to include the new element
        #this is simulating our baskets only holding 2 types of fruits and the moment we include a new type we must remove an old type from consideration (if the count of that fruit drops to 0) to 
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

            while len(buckets) > 2:
                curr_fruits -= 1
                buckets[fruits[left]] -= 1
                #means we have successfully shrunk our window to not consider old fruit type and start considering new fruit type thats being added so remove old fruit type aka the fruit at left from our basket 
                if buckets[fruits[left]] == 0:
                    buckets.pop(fruits[left])
                left += 1
            
            max_fruits = max(max_fruits, curr_fruits)
        
        return max_fruits 

        #complexity:
        #time: O(n) stepping thru the array at most 2n times which simplifies to n
        #space: O(1) as our hashmap always holds at most a constant number of keys aka 2

