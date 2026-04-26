class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            char_r = s2[r]
            while char_r not in count or count[char_r] == 0:
                if l < r:
                    if s2[l] in count:
                        count[s2[l]] += 1
                    l += 1
                else:
                    l = r + 1
                    break
            else:
                count[char_r] -= 1
                if (r - l + 1) == len(s1):
                    return True

        return False
