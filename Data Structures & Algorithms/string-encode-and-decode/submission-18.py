class Solution:
    '''
    ex:
    strs = ["Hello","World"]
    
    We will use number of chars per word + # as our deliminter as it tells us how much of the encoded string to read to after the deliminter allowing us to extract the word 

    encode -> 5#Hello5#World
    decode -> idenitfy where first #, get the number of chars to extract from the string to turn into a word on the left and then append that to our answer list
    '''
    
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded
    
    #5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []

        #instead of creating new encoded str slices to iterate thru use a ptr to iterate thru og encoded string
        i = 0

        while i < len(s):

            #find # delim
            j = s.find('#', i)
      
            len_of_word = int(s[i:j])

            word = s[j + 1:j + 1 + len_of_word]
            res.append(word)

            i = j + 1 + len_of_word
        return res