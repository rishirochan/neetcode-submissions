class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, current = [], []
        
        def dfs(i, total):
            if total == target:
                res.append(current[:])
                
            elif total > target:
                return
            
            for j in range(i, len(nums)):
                current.append(nums[j])
                dfs(j, total + nums[j])
                current.pop()

        dfs(0, 0)
        return res