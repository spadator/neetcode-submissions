class Solution:
    def trap(self, height: List[int]) -> int:
        trapWater = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                trapWater += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                trapWater += maxRight - height[r]

        return trapWater