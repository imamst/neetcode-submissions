class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCharCount, tCharCount = {}, {}

        for i in range(len(s)): # will create [1, 2, 3, 4....] for index
            sCharCount[s[i]] = 1 + sCharCount.get(s[i], 0)
            tCharCount[t[i]] = 1 + tCharCount.get(t[i], 0)
        
        return sCharCount == tCharCount