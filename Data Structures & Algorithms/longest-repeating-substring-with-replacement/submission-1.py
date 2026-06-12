class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sl = 0
        counter = Counter()
        res = 0

        for f in range(len(s)):
            counter[s[f]] += 1
            #f += 1

            while (f - sl + 1) - max(counter.values()) > k:
                counter[s[sl]] -= 1
                sl += 1
                
            res = max(res, f - sl + 1)
        return res

