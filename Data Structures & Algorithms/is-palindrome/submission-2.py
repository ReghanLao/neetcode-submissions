class Solution:
    def isPalindrome(self, s: str) -> bool:
        #confirm that the front and the back of the string are simultaneously the same
        #step by step   

        #convert into a lowercase alphanumeric string 
        al_num = []
        for char in s:
            if char.isalnum():
                al_num.append(char.lower())
        
        cleaned = "".join(al_num)
        
        #have two ptrs start from left and right and confirm equality 
        left = 0 
        right = len(cleaned) - 1

        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True 