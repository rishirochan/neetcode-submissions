class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, current = [], []
        
        def dfs(i, total):
            if i >= len(nums) or total > target:
                return
            elif total == target:
                res.append(current[:])
                return
            
            current.append(nums[i])
            dfs(i, total + nums[i])
            current.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res