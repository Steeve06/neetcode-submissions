class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - Check if both strings have same length if not return false
        - Create two arrays to store each character and their freq
        - Calculate the number of characters that have their matches in both arrays
        - Initialize left pointer
        - Right pointer navigates in range btw len(s1) and len(s2)
        - If matches == 26 i return true else:
        - I move onto the next character in s2, increase its count in corresponding array
        - If this count matches with its counter part in first array, increase matches by one
        - Else, check if the count at index in first array +1 equals that of that elmt in 2nd array
        - If it is the case, matches decrease by one
        - Update the left end. If elmt at index of left, has same count as that elmt in other array
        - add matches else decrease and update l
        
        """
        s1count,s2count = [0]*26,[0]*26
        matches = 0
        l = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1count[ord(s1[i])- ord("a")] += 1
            s2count[ord(s2[i])- ord("a")] += 1 

        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
            else:
                matches += 0

        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2count[index] += 1

            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2count[index] -= 1

            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        
        return matches == 26


        

        



