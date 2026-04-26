class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        tCount = {}
        window = {}
        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        have, need = 0, len(tCount)        
        l = 0
        shorter, shorterLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                if (r - l + 1) < shorterLen:
                    shorter = [l, r]
                    shorterLen = (r - l + 1)
                window[s[l]] -= 1 
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        
        return s[shorter[0]:shorter[1]+1] if shorterLen != float("infinity") else ""
