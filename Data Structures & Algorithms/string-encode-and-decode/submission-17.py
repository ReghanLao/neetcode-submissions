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
        encoded = s
        res = []

        if len(encoded) == 0:
            return []

        #continue extracting words while encoded is not empty aka while i is less than len of encoded 
        while True:
            #ptr indicating the start of the string we will iterate over
            i = encoded.find('#') + 1 

            #len of word to extract from string
            len_of_word = int(encoded[:encoded.find('#')])
 
            word = encoded[i:i + len_of_word]
            res.append(word)
          
            
            encoded = encoded[i + len_of_word:]
         
            #there are no more words to extract 
            if encoded == "":
                break

        return res