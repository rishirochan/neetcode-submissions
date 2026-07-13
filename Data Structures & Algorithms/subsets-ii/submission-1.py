class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, current):
            res.append(current[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                current.append(nums[j])
                dfs(j+1, current)
                current.pop()

        
        dfs(0, [])
        return res