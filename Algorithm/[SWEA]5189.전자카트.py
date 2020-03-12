import math

class FINDMIN:  #함수가 끝나며 이전 int타입 최소값과 대조해야 하므로 class 선언하여 self.min을 정의한다.
    def __init__(self,n,table):
        self.n = n #테이블 크기
        self.min = math.inf #min값. inf로 초기화
        self.table = table #배터리 소비량 테이블

    def DFS(self,res,n_pre,cdd_set):
        if not cdd_set:
            res += table[n_pre][0]  # 관리구역 -> 사무실 복귀 배터리소비
            if self.min > res:
                self.min = res
            return

        for i in cdd_set:
            self.DFS(res+self.table[n_pre][i],i,cdd_set-{i})


test = int(input())

for t in range(test):
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(n)]

    ccl = FINDMIN(n,table)
    ccl.DFS(0,0,set(range(1,n))) #초기 위치 사무실이므로 0으로 설정.
    print("#{} {}".format(t+1,ccl.min))
