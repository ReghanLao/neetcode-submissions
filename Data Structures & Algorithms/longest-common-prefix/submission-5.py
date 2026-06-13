class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we can only check for common prefixes up to min length 
        # where min length is the length of the shortest word 

        min_length = math.inf
        prefix = ''
        lcp = ''

        for word in strs:
            min_length = min(len(word), min_length)
        
        #for a common prefix to exist: ALL words MUST have the same prefix 
        #lets compare the prefix of a current word to the first word
        #this lets us ensure that we satisfy that ALL words must have the same prefix 
        for i in range(min_length):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    #our longest common prefix ends here 
                    return lcp 
                else: 
                    prefix = strs[0][i]
            
            lcp += prefix 

        return lcp 
        

