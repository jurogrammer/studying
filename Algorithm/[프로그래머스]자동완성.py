class Node:
    def __init__(self):
        self.isOne = True
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        curNode = self.root

        for w in word:
            if w in curNode.children:
                curNode.children[w].isOne = False
            else:
                curNode.children[w] = Node()
            curNode = curNode.children[w]

    def getInputCount(self,word):
        curNode = self.root
        cnt = 0
        for w in word:
            curNode = curNode.children[w]
            cnt += 1
            if curNode.isOne:
                return cnt
        return cnt


def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    answer = 0
    for word in words:
        answer += trie.getInputCount(word)
    return answer

words = ["go","gone","guild"]
print(solution(words))