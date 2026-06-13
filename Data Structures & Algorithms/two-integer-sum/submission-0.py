class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dictionary to store the difference between target and current elemenet
        #if the difference between target and current element exists in the dict then we have
        #found two numbers which add up to target (current element and the difference stored in the dict)

        diff = {}
        n = len(nums)

        for i in range(n):
            difference = target - nums[i]
            if difference in diff:
                return [diff[difference], i]
            else: 
                diff[nums[i]] = i
    