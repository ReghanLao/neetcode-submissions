class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""

        for word in strs:
            len_of_word = len(word)
            new += str(len_of_word) + "#" + word 

        return new 
        
    def decode(self, s: str) -> List[str]:
        res = []

        while s:
            pivot = s.find("#")
            num_of_chars = int(s[0:pivot])

            #we begin extracting at pivot + 1 
            word = s[pivot + 1:pivot + 1 + num_of_chars]
            res.append(word)
            
            s = s[pivot + 1 + num_of_chars:]
            
        return res