class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Brute force:
        For every pair of start and end indicies in the str (i -> j) aka every 
        possible substring we can obviously perform k replacements if possible
        in this range to ultimately get the longest substring that contains only one
        distinct character 

        But going through every single possible substring is expensive and performs
        unnecessary work lets take 

        XYYX as an example where k = 2

        In our first iteration we are able to see that we can perform two replacements to get the longest substring that only contains one character so why would we need to go thru the remaining substrings that are possible. its a waste

        Alternative:

        We don't need to evaluate all possible substrings to determine whats the 
        longest substring with one character after performing k replacements 
        
        we can just use a sliding window to consider the string we can build up to 
        a certain point and determine what the longest substring with one distinct
        char is after performing k replacements

        if the number of replacements needed to match the most frequent character
        exceeds k then we have to go ahead and consider a new substring - move
        window bounds

        by doing this we eliminate unnecessary work - checking substrings that will
        never gives us an answer 

        We will also need to keep track of the frequency of all characters in the 
        current stream aka window to see what character to match to to maximize the
        longest substring with one distinct character 
        '''
        #key -> int (default is 0)
        counts = defaultdict(int)

        #evaluate substrings through our window bounds
        left = 0 

        best = -math.inf

        for right in range(len(s)):
            #steps are to first account for the character coming into our substring or window, then to see what the most frequent in our window is, see if we can perform k replacements to match that most frequent character if so our current window is the longest possible substring after performing k replacements that has one distinct char, if not then we need to consider a new substring so continously shrink from our window until we are able to perform k replacements to match the most frequent character
            counts[s[right]] += 1

            most_freq = max(counts.values())

            num_of_replacements = (right - left + 1) - most_freq

            while num_of_replacements > k:
                counts[s[left]] -= 1
                left += 1

                most_freq = max(counts.values())
                num_of_replacements = (right - left + 1) - most_freq




            best = max(best, (right - left + 1))

        return best

