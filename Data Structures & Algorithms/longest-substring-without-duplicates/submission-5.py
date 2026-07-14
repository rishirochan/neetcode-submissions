class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = 0
        hold = set()
        res = 0

        for f in range(len(s)):
            while s[f] in hold:
                hold.remove(s[sl])
                sl += 1
            hold.add(s[f])
            res = max(res, f - sl + 1)

        return res

                
            

                
