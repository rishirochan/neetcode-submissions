class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenn = len(nums)
        l1 = [1] * lenn
        l2 = [1] * lenn
        res = [0] * lenn

        for i in range(1, lenn):
            l1[i] = l1[i - 1] * nums[i - 1]

        for i in range(lenn - 2, -1, -1):
            l2[i] = l2[i + 1] * nums[i + 1]
        
        for i in range(lenn):
            res[i] = l1[i] * l2[i]
        
        return res