class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCharCount = {}
        tCharCount = {}

        for x in s:
            sCharCount[x] = sCharCount.get(x, 0) + 1
        
        for y in t:
            tCharCount[y] = tCharCount.get(y, 0) + 1

        for z in sCharCount:
            if sCharCount.get(z, 0) != tCharCount.get(z, 0):
                return False
        
        return True