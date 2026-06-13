class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        #to make sure that these pointers do not cross because 
        #these indicies cannot be equal - two distinct solutions

        while left < right:
            result = numbers[left] + numbers[right]

            if result == target:
                return [left + 1, right + 1]
            elif result > target:
                #we need to move right pointer more to the left to 
                #decrease the overall sum 
                right -= 1
            else:
                left += 1
        


