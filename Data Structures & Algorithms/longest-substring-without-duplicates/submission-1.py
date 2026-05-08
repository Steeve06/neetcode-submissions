class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        - Create a set from which i will add or remove the letters
        - Initialize left pointer to O
        - Navigate through string with right array
        - while character at s[r] is found in set, I remove it from the set and increment l
        - Else I add the character.
        - Compute the length of longest xter by max(res,r-l+1)
        
        """
        charSet = set()
        l=0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result,r-l+1)
        return result

        


       


       