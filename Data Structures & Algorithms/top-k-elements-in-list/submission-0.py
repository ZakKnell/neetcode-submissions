class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        answer = []
        buckets = [ [] for _ in range(len(nums) + 1) ]

        for i, n in enumerate(nums):
            d[n] = d.get(n, 0) + 1
        
        for key in d:
            buckets[d[key]].append(key)
        
        count = 0
        for i in range(len(buckets) - 1, 0, -1):
            for item in buckets[i]:
                count += 1
                answer.append(item)
                if count >= k:
                    return answer
                