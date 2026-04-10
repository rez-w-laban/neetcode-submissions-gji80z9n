class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #bf
        res = 0

        for i in range(len(s)):
            sett = set()
            for j in range(i, len(s)):
                if s[j] in sett:
                    break
                sett.add(s[j])
            res = max(res, len(sett))
        return res