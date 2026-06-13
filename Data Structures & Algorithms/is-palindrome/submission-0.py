import string 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #formatting input str to alphanumeric str without whitespace
        alpha_num = set(string.ascii_letters + string.digits)
        alpha_num_string = ""
        for char in s:
            if char in alpha_num:
                alpha_num_string += char
        formatted_str = alpha_num_string.lower()

        left = 0 
        right = len(formatted_str) - 1

        while left <= right:
            if formatted_str[left] != formatted_str[right]:
                return False
            
            left += 1
            right -=1 
        
        return True

