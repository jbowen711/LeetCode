class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currA = 0
        n = len(heights)
        l, r = 0, n - 1

        while (l < r):
            y = min(heights[l], heights[r])
            x = r - l
            area = x * y
            if (area > currA):
                currA = area
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1

        return currA
