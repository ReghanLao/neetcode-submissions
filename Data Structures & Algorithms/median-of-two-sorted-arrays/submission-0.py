import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        #want to run BS on the smaller array 
        if len(B) < len(A):
            A = nums2
            B = nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        left = 0
        right = len(A) - 1

        #while we haven't found a valid minimum yet 
        while True:
            #end index for Aleft
            i = (left + right) // 2 #A
            #end index for Bleft
            j = half - i - 2 #B

            #define boundary elements
            Aleft = A[i] if i >= 0 else -math.inf
            Aright = A[i + 1] if (i + 1) < len(A) else math.inf
            Bleft = B[j] if j >= 0 else -math.inf
            Bright = B[j + 1] if (j + 1) < len(B) else math.inf

            #validate left partition else modify partition thru BS
            if Aleft <= Bright and Bleft <= Aright:
                #even length merged arr median is 
                #max(Aleft,Bleft) + min(Aright, Bright) / 2
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
                else:
                #odd length median is min(Aright, Bright) because 
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1



