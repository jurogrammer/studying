'''
https://jurogrammer.tistory.com/19
'''
def solution(n, computers):
    parents = [i for i in range(n)]

    def FindRoot(node):
        parentNode = parents[node]
        if parentNode != node:
            return FindRoot(parentNode)
        else:
            return parentNode

    def UnionSet(node1, node2):
        rootNode1 = FindRoot(node1)
        rootNode2 = FindRoot(node2)
        if rootNode1 == rootNode2:
            return
        else:
            parents[rootNode1] = rootNode2
            return

    def CountRoot(parents):
        roots = set()
        for i in range(n):
            roots.add(FindRoot(i))

        return len(set(roots))

    for node1 in range(n):
        for node2 in range(node1,n):
            if computers[node1][node2]:
                UnionSet(node1, node2)

    return CountRoot(parents)
