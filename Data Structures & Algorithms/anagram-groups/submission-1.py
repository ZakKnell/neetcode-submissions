class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for word in strs:
            frequency = [0] * 26
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            key = tuple(frequency)
            if key in answer:
                answer[key].append(word) 
            else:
                answer[key] = [word]
        return list(answer.values())