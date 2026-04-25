class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxLength = 1
        l, r = 0, 1

        while r < len(s):
            if s[r] not in s[l:r]:
                maxLength = max(maxLength, r - l + 1)
            else:
                while l < r and s[l] != s[r]:
                    l += 1
                l += 1
            r += 1
        
        return maxLength
