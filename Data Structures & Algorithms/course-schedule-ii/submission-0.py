class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visit = set()
        completed = set()
        order = []

        def dfs(course):
            if course in visit:
                return False
            if course in completed:
                return True
            
            visit.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            completed.add(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
