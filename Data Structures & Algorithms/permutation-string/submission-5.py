class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we are maintaining a fixed size window of length s1
        #in the window that we slide over s2 we want to check
        #if that window contains the same character counts as s1

        #edge case: if the length of s1 is greater than s2
        #we cannot check for permutations in s2 as they will never exit
        if len(s1) > len(s2):
            return False 
            
        s1_counts = {}
        s2_counts = {}
        
        for i in range(len(s1)):
            if s1[i] in s1_counts:
                s1_counts[s1[i]] += 1
            else:
                s1_counts[s1[i]] = 1
            
            if s2[i] in s2_counts:
                s2_counts[s2[i]] += 1
            else:
                s2_counts[s2[i]] = 1

        if s1_counts == s2_counts:
            return True
        
        for right in range(len(s1), len(s2)):
            #add incoming char @ right
            if s2[right] in s2_counts:
                s2_counts[s2[right]] += 1
            else:
                s2_counts[s2[right]] = 1
            
            #remove outbound char
            s2_counts[s2[right - len(s1)]] -= 1

            #if count of outbound char goes to zero please delete key
            if s2_counts[s2[right - len(s1)]] == 0:
                del s2_counts[s2[right - len(s1)]]

            #check current window if s2 contains permutation of s1
            if s1_counts == s2_counts:
                return True
        
        return False 


            
            

        


            
            
