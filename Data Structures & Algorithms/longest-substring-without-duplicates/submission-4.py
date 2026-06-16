class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = 0
        hold = set()
        ans = 0
        
        for f in range(len(s)):
            while s[f] in hold:
                hold.remove(s[sl])
                sl += 1
            hold.add(s[f])
            ans = max(ans, f - sl + 1)

        return ans

                
            

                
