class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current):
            if len(current) >= len(nums):
                res.append(current[:])
                return
            
            for j in range(len(nums)):
                if nums[j] in current:
                    continue
                current.append(nums[j])
                dfs(current)
                current.pop()
        
        dfs([])
        return res