class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap = defaultdict(list)
        for edgea, edgeb in edges:
            premap[edgea].append(edgeb)
            premap[edgeb].append(edgea)
        visit = set()
        res = 0

        def dfs(node):
            visit.add(node)
            for nex in premap[node]:
                if nex not in visit:
                    dfs(nex)

        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res