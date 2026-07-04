class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            one solution is to check every possible substring
            starting at i going down to j 

            but thats too inefficient 

            instead it would be more efficient to go thru this
            string character by character in a contingous manner
            and detect whether or not there is a dup in our current
            substring we are looking at 

            thus we use a sliding window 

            if there is a duplicate that violates our window condition
            we want only substrings without duplicates so we 
            modify our window st we remove characters from the beginning of our window
            til the duplicate no longer exists in this way we are also considering
            future unique sols as well
        '''

        left = 0 
        seen = set()
        best = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
            
            seen.add(s[right])

            window_size = right - left + 1
            best = max(window_size, best)
        
        return best 

