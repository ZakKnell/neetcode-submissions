class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1frequency = [0] * 26
        for char in s1:
            s1frequency[ord(char) - ord('a')] += 1
        
        s2frequency = [0] * 26
        for char in s2[:len(s1)]:
            s2frequency[ord(char) - ord('a')] += 1

        if s2frequency == s1frequency:
            return True 

        left = 0
        for right in range(len(s1), len(s2)):
            
            s2frequency[ord(s2[right]) - ord('a')] += 1
            s2frequency[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if s2frequency == s1frequency:
                return True
        return False

            
            


