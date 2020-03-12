'''
문제풀이 방식. Top-Down
매단계 왼쪽카드, 오른쪽카드의 순서에 따라 값이 결정된다. 즉, 변수 2개로 최적 값이 결정.
따라서 j번째 단계, j-1단계를 보면, f(leftIdx(j),rightIdx(j)) = max(f(leftIdx(j-1),rightIdx(j-1)),
                                                                f(leftIdx(j-1),rightIdx(j)),
                                                                f(leftIdx(j),rightIdx(j-1))+Value(j) (단, 마지막 경우는 왼쪽이 오른쪽보다 클 떄.)
라고 정의할 수 있음.
baseCase는 카드게임이 종료되는 시점인 0인 지점.

'''

memo = {} #메모할 dict타입 변수 선언

n = int(input()) #카드의 수 input

leftCards = [0] + list(map(int, input().split())) #Card의 값을 담고 있는 list타입 변수. index는 카드의 순서를 나타낸다.
                                                  #첫번째 카드까지 있다고 보기 위해 0번 인덱스 dump값 넣음.
rightCards = [0] + list(map(int, input().split()))

def getVal(leftIdx,rightIdx,val):
    if (leftIdx,rightIdx) in memo:   #메모에 값이 있는 경우엔 반환
        return memo[(leftIdx,rightIdx)]


    else:
        if leftIdx == 0 or rightIdx == 0: #메모에 값이 없는데, baseCase에 도달한다면 메모에 값 입력 후 종료.
            memo[(leftIdx, rightIdx)] = val
            return memo[(leftIdx,rightIdx)]

        else:                                             #inductive part : 점수받는 경우(1가지), 못받는경우(2가지)
            if leftCards[leftIdx] > rightCards[rightIdx]: #  #점수획득하는 경우.
                temp = getVal(leftIdx, rightIdx-1, val+rightCards[rightIdx])
            else:
                temp = 0 #점수를 받을 수 있는 상황이 아니라면 0으로 선택 불가능하게 넣기. 문제조건은 양의정수이므로
            memo[(leftIdx,rightIdx)] = max(getVal(leftIdx-1, rightIdx,val),getVal(leftIdx-1, rightIdx-1,val),temp)
            return memo[(leftIdx,rightIdx)]

print(getVal(n,n,0))    #내가 최종적으로 구하고 싶은 값은 leftIdx,rightIdx가 n,n일때. 따라서 n,n대입
                        #val의 초기값은 0. 베이스케이스에 도달할 때까지 점수획득할 때 val값 증가.

