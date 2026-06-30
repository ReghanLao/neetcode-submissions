class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            utlize the sorted nature of input array to avoid
            comparing pair wise elements 

            since our index1 < indew2 we can start two ptrs starting
            at the two corners of the array (start and end)

            if our sum is too small adjust our left ptr up by one
            if our sum is too big adjust our right ptr down by one

            eventually we will land upon a sol
        '''

        left = 0
        right = len(numbers) - 1

        while left < right:
            calculated_sum = numbers[left] + numbers[right]

            if calculated_sum == target:
                return [left + 1, right + 1]
            elif calculated_sum < target:
                left += 1
            else: 
                right -= 1 
            