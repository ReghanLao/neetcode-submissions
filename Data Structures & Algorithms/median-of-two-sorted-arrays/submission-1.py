import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        total = len(nums1) + len(nums2)
        half = total // 2 #defines size of the left partition 

        left = 0 
        right = len(A) - 1

        #while we have't found a median lets go and compute
        #these partitions via BS so that we are able to 
        #extract the median and return it
        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i + 1] if i + 1 < len(A) else math.inf 
            Bleft = B[j] if j >= 0 else -math.inf
            Bright = B[j + 1] if j + 1 < len(B) else math.inf

            if Aleft <= Bright and Bleft <= Aright:
                #we have a valid left partition so lets compute median
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1

