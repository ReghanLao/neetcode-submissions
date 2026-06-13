from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we are going to count the occurences of each num and then sort the dict 
        #produced by that process and populate and auxilary array with the appropriate number of 0,1,2s
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda x:x[0]))

        #create aux array
        res = []

        #for every key(0,1,2) we want to go thru it how many times it occurs and append the key that many times to the aux array
        for key, val in sorted_count.items():
            for _ in range(val):
                res.append(key)
        
        #copy values from res to nums
        #note: res and nums will be of the same size 
        for i in range(len(nums)):
            nums[i] = res[i]

