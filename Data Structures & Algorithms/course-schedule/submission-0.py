class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for crs, rec in prerequisites:
            premap[crs].append(rec)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if premap[course] == []:
                return True
            visited.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            premap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        
