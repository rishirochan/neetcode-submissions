class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if not n:
        #     return True

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for val in graph[node]:
                if val == parent:
                    continue
                if not dfs(val, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n