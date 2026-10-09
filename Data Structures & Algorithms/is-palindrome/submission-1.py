class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char

        left = 0
        right = len(cleaned) -1
        while left <= right:
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            else:
                return False
        return True