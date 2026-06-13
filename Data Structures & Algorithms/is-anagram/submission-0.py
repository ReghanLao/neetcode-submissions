class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram -> word with same character frequencies -> use hashmap 

        s_freq = {}
        t_freq = {}

        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1
        
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1
        
        return s_freq == t_freq