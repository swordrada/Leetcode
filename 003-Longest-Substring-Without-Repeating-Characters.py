class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            # When find a repeat word, slice the start window to next index.
            start = max(start, maps.get(s[i], -1) + 1)
            res = max(res, i - start + 1)
            # Record every word's index place.
            maps[s[i]] = i
        return res
