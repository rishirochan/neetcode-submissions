class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visit = set()
        order = []

        def dfs(course):
            if course in visit:
                return False
            if premap[course] == []:
                if course not in order:
                    order.append(course)
                return True
            
            visit.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            order.append(course)
            premap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
