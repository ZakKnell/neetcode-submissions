class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            key = tuple(counts)
            if key in ans:
                ans[key].append(word)
            else:
                ans[key] = [word]
        return list(ans.values())