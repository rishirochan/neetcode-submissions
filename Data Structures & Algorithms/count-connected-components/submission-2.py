class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap = defaultdict(list)
        for edgea, edgeb in edges:
            premap[edgea].append(edgeb)
            premap[edgeb].append(edgea)
        visited = set()
        res = 0

        def dfs(edge):
            visited.add(edge)
            for con in premap[edge]:
                if con not in visited:
                    dfs(con)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
