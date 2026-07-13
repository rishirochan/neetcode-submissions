class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for c, p in prerequisites:
            premap[c].append(p)
        visit = set()
        completion = set()

        def dfs(course):
            if course in visit:
                return False
            if course in completion:
                return True
            
            visit.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            completion.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                


     

        
