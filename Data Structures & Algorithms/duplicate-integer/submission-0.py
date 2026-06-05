class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            s_initial = len(s)
            s.add(num)
            s_after = len(s)

            if s_initial == s_after:
                return True
        
        return False
                