class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for char in s:
            sdict[char] = sdict.get(char, 0) + 1
        
        tdict = {}
        for char in t:
            tdict[char] = tdict.get(char, 0) + 1
        
        if sdict == tdict:
            return True
        return False