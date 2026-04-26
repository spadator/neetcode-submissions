class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            # pop smaller values from q
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output

            
