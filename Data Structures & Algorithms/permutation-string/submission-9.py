from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Basically we want to see if there exists a
            permutated version of s1 in any of s2's substrings 

            Brute Force:
            We can go through every single possible substring
            formed from i to j and check for the existence of a permutation

            But the problem is that we perform useless work, our s1 string
            is only a given length why would we ever want to check substrings
            that are greater in length or shorter in length

            Thus we propose a fixed size sliding window which will 
            capture each substring that is of equal size to s1 in s2
            and at each window we ask is this window/substring capturing a 
            permutation of s1 if so then we have found a permutation of s1 in 
            s2 and we return true else we go thru every single window or substring
            of size s1's length and we find no permutations thus we return false

            we checking for permutations we can check the count of both substrings
        """

        left = 0
        window_size = len(s1)

        s1_counts = Counter(s1)

        counts = {}

        for right in range(len(s2)):
            curr_window_len = right - left + 1

            #we are only considering fix sized windows 
            #because we only care about substrings that are 
            #of size s1 when checking for permutations 
            if curr_window_len > window_size:
                counts[s2[left]] -= 1
                
                if counts[s2[left]] <= 0:
                    counts.pop(s2[left])
                
                left += 1

                curr_window_len = right - left + 1 
            
            counts[s2[right]] = counts.get(s2[right], 0) + 1

        
            if counts == s1_counts:
                return True

        return False
        

            