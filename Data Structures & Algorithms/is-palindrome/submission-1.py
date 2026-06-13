import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case_letters = set(string.ascii_lowercase)
        upper_case_letters = set(string.ascii_uppercase)
        numbers = {'0','1','2','3','4','5','6','7','8','9'}

        alpha_string = ""

        for char in s:
            if char in lower_case_letters or char in upper_case_letters or char in numbers:
                alpha_string += char.lower()

        left = 0 
        right = len(alpha_string) - 1

        while left <= right:
            if alpha_string[left] != alpha_string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True 
        
