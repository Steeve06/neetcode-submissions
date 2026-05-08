class Solution:
    """
    - to encode, in an array save length of each word followed by the # and word
    - to decode, loop through new array
    - if loop id is < len or array continue
    - if loop id arrives at # then next is the word
    
    
    """
    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s)) + "#" + s
        return word
    
    def decode(self, s: str):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j 
        return res
            





