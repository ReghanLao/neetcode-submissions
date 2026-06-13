class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_copy = []

        for num in nums: 
            nums_copy.append(num)
        
        #when rotating an array we rotate every element by k
        #but note that rotating by k is the same as rotating by 
        # (k % n) where n is the len of input 

        #compute new posiiton of the elements as a result of shifting 

        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = nums_copy[i]
        