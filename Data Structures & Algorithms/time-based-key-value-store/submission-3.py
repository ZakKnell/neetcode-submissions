class TimeMap:

    def __init__(self):
        self.timemap: dict[str, tuple[list[str], list[int]]] = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = ([value], [timestamp])
        else:
            self.timemap[key][0].append(value)
            self.timemap[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        def binarySearch(left, right, target, nums) -> int:
            l, r = left, right
            if l > r:
                return r

            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m - 1
                return binarySearch(l, r, target, nums)
            
            return binarySearch(m + 1, r, target, nums) 

        if key not in self.timemap:
            return ""
        timestamps = self.timemap[key][1]

        left = 0
        right = len(timestamps) - 1
        index = binarySearch(left, right, timestamp, timestamps)
        if index == -1:
            return ""
        return self.timemap[key][0][index]

