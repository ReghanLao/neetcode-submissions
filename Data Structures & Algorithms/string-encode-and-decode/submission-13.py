class Solution:
    
    #when encoding the string we want to encode it in some type of way
    #st it will help us later to decode it -> use a special deliminter
    #that is not confined by the ASCII constraint  
    def encode(self, strs: List[str]) -> str:
        #use length + # deliminator and place this before every string 
        #length will tell us how many characters to extract after # symbol
        # length + # isn't confined by the ASCII constraint either as its a unique combo not in native ASCII
        encoded_string = ""

        for word in strs:
            encoded_string += f"{len(word)}#{word}"

        return encoded_string

    #used the encoded strings properties to extract words 
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        #2#Hi#10abcdefghij
        while i < len(s):
            #extract from ptr down to the last character specified by length
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        
        return res
