class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortedNums = sorted(nums)

        for i, n in enumerate(sortedNums):
            if n > 0:
                break

            if (i > 0) and n == sortedNums[i-1]:
                continue
            
            l, r = i+1, len(sortedNums)-1
            add = n + sortedNums[l] + sortedNums[r]
            while l < r:
                add = n + sortedNums[l] + sortedNums[r]
                if add < 0:
                    l += 1 
                elif add > 0:
                    r -= 1
                else:
                    res.append([n, sortedNums[l], sortedNums[r]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l-1] and l < r:
                        l += 1
            
        return res
            

