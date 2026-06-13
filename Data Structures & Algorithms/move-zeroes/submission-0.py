class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0 

        #1st pass to place non zero numbers in their correct relative order positoin 
        for i in range(len(nums)):
            if nums[i] != 0:
                #if our current number is a non zero number lets insert it into our 
                #next non zero position 

                nums[insert] = nums[i]
                insert += 1
        
        #second pass to 'push' all zeroes to the end 
        for i in range(insert, len(nums)):
            nums[i] = 0
        
        
        