class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find two numbers x and y st x + y = target 
        #target - x = y
        #if we go through the array and we keep track of every
        #number we have seen so far, we have a way to check 
        #whether or not this equation target - x = y is true 
        
        #map number to index 
        seen = {}

        for i in range(len(nums)):
            #x is nums[i]
            if target - nums[i] in seen:
                j = seen[target - nums[i]]
                return [j, i]
            
            seen[nums[i]] = i
            

