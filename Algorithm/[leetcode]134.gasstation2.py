class Solution:
    def canCompleteCircuit(self, gas, cost) :
        n = len(gas)
        new = [gas[i] - cost[i] for i in range(n)]

        if sum(new) < 0:
            return -1

        for sIdx in range(n):
            if new[sIdx] < 0:
                continue
            else:
                amount = 0
                i = sIdx
                flag = True
                for d in range(n):
                    i = (i+d)%n
                    amount += new[i]
                    if amount < 0:
                        flag = False
                        break

                if flag:
                    return sIdx
s = Solution()
gas= [5,1,2,3,4]
cost = [4,4,1,5,1]
print(s.canCompleteCircuit(gas,cost))