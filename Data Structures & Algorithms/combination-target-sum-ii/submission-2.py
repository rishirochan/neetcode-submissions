class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, current):
            if total == target:
                res.append(current[:])
            if total >= target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                current.append(candidates[j])
                dfs(j+1, total + candidates[j], current)
                current.pop()
        
        dfs(0, 0, [])
        return res