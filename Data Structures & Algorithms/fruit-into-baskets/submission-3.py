class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #fruits[i] -> type of fruit produced
        #two baskets where each basket can only hold one fruit type 
        #we have a hashmap that maps fruit type to number of fruit 
        #basically our hashmap represents our buckets 
        #if the number of fruit types exceed two then we need to prune from this hashmap (keep removing from the front of the window until we have two unique fruit types remaining)
        #since we are forced to pick we are also forced to prune in the event that pruning needs to happen 

        buckets = {}
        left = 0

        #at the very minimum we can pick 1 fruit type 
        max_fruits = 1
        
        curr_fruits = 0

        for right in range(len(fruits)):        
            if fruits[right] in buckets:
                buckets[fruits[right]] += 1
            else:
                buckets[fruits[right]] = 1

            curr_fruits += 1

            while len(buckets) > 2:
                buckets[fruits[left]] -= 1

                if buckets[fruits[left]] == 0:
                    del buckets[fruits[left]]
                
                curr_fruits -= 1
                print(curr_fruits)
                left += 1

            max_fruits = max(max_fruits, curr_fruits)
        print(buckets)
        return max_fruits
        