class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - Create two pointers, one for first elmt and other for last elmt
        - While the first elmt pointer is less than the last elmt pointer
        - Check whether or not these pointers point to spaces or non alphanumeric
        - If it is the case, increase and decrease their lengths by 1 resp
        - Now, check if the values pointes by both are the same.
        - If not, return false.
        - Update the pointers value
        - If not also return false
        - Create an alphanum function by comparing the ord(c) with those of 
        - A-Z, a-z and 0-9.
        """

        l = 0
        r = len(s) - 1

        while l<r:
            while l<r and not self.alpha(s[l]):
                l += 1
            while l<r and not self.alpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
        

    def alpha(self,c):
        if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9"):
            return True

