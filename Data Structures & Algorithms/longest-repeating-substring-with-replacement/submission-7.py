class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            We don't actually need to literally replace the 
            characters in the string.

            We want to evaluate every subportion of the string to 
            see where we can optimize returns on performing k replacements

            Going through every pair of substrings is inefficient 
            since we are restricted to only k replacements - starting at 
            a particular index and considering the substring built by going to the
            last index by performing k replacements might not change anything
            after a while 

            eg:
            abbc, k = 1
            bbbc, i = 0 (evaluating every single possible substring from index 0)
            abbb, i = 1 (evaluating every single possible substring from index 1)
            but all of these dont change the fact our longest repeating substring will be bbb

            so we should tackle this linearly with a sliding window 

            We can simulate by counting the given characters in a 
            subportion of the string we are going through and 
            seeing how much characters are alloted to be used to match
            the most frequent character in this subportion 
            
            this removes the need to unnecesarily check every possible pair of 
            substrings 

            once the number of replacements in the current window exceeds what
            we are allotted to we shrink the window til alotted is >= required

            continously compute window size for longest substring
        '''

        #dynamically keep track of char counts in window
        counts = {}

        left = 0 

        best = 1 

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            window_size = right - left + 1
            max_freq = max(counts.values())
            required = window_size - max_freq

            #determine the number of replacements we need to make
            #size of window - max_freq

            #if required is greater than allotted shrink window to consider new 
            #possible sols in the future

            #recompute required as necessary 
            while required > k:
                counts[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                max_freq = max(counts.values())

                required = window_size - max_freq 
            
            best = max(window_size, best)
        
        return best 


