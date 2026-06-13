class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length 
        return res


