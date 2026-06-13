from collections import Counter 

#basically a string s1 is a permutation of a string s2 if both
#have the same character counts at a very raw bones level 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case: if the length of s2 is less than s1 then s2 could never contain a permutation of s1
        if len(s2) < len(s1):
            return False

        s1_counts = Counter(s1)
        s2_counts = {}
        
        #go thru the first window of s2 to check for permutation
        for i in range(len(s1)):
            s2_counts[s2[i]] = s2_counts.get(s2[i], 0) + 1

        #if there is a permutation in the first k elements return true 
        if s1_counts == s2_counts: 
            return True 

        left = 0 
        #else we slide thru the remaining s2 we check at every given window size 
        #is there a permutation of s1 in the window (counts are the same) then return true
        for right in range(len(s1), len(s2)):
            s2_counts[s2[left]] -= 1
            #for dictionary equality to be true every single kvp must match
            #so if a dict's key's value 0 just del it so we can ensure equality check isnt being messed wit
            if s2_counts[s2[left]] == 0:
                del s2_counts[s2[left]]
            left += 1
            s2_counts[s2[right]] = s2_counts.get(s2[right], 0) + 1
            print(s2_counts)
            print(s1_counts)
            if s1_counts == s2_counts: 
                return True 
        
        return False

