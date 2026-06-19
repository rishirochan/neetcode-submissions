class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(a, b, visited):
            if a == b:
                return True
            visited.add(a)
            for val in graph[a]:
                if val not in visited:
                    if dfs(val, b, visited):
                        return True
            return False

        for a, b in edges:
            if graph and dfs(a, b, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        
