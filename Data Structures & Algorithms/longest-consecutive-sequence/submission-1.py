class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for i in seen:
            if i - 1 not in seen:
                length = 1
                while i + length in seen:
                    length += 1
                res = max(res, length)

        return res
        