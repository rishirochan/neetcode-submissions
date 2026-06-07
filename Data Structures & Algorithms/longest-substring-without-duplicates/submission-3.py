class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = 0
        f = 0
        hold = set()
        res = 0
        
        while f < len(s):
            if s[f] not in hold:
                hold.add(s[f])
                f += 1
                res = max(res, f - sl)
            else:
                hold.remove(s[sl])
                sl += 1
                
        return res

                
