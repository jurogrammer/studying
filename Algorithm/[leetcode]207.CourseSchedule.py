class Solution:
    def canFinish(self, numCourses, prerequisites):
        parents = [set() for _ in range(numCourses)]
        for c, p in prerequisites:
            parents[c].add(p)

        visited = 0
        for node in range(numCourses):
            if visited & (1 << node):
                continue
            curNode = node
            while True:
                visited = visited | 1 << curNode
                nextNode = parents[curNode]
                fgdf;l
                if nextNode == node:
                    return False
                if nextNode == -1:
                    break
                curNode = nextNode

        return True

s = Solution()
print(s.canFinish(3,[[1,0],[1,2],[0,1]]))