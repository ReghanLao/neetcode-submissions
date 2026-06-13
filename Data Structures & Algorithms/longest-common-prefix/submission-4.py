class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #go through every alligned index and check if characters at 
        #alligned index is equal
        if len(strs) == 1:
            return strs[0]
        #the shortest word is the bottleneck for how far we go iterate our alligned indices
        min_alligned = math.inf
        lcp = ""
        common_prefix = True
        prefix = ""

        for word in strs:
            min_alligned = min(len(word), min_alligned)
        print(min_alligned)
        for i in range(min_alligned):
            common_prefix = True

            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    common_prefix = False 
                else: 
                    prefix = strs[j][i]
            
            if common_prefix:
                lcp += prefix
            else:
                break 

        return lcp 
