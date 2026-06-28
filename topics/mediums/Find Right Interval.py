class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []

        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))

        starts.sort()

        def lower_bound(target):
            left = 0
            right = len(starts)

            while left < right:
                mid = (left + right) // 2

                if starts[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        result = []

        for start, end in intervals:
            pos = lower_bound(end)

            if pos == len(starts):
                result.append(-1)
            else:
                result.append(starts[pos][1])

        return result