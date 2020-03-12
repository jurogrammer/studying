'''
탐색방법은 각 숫자마다 +할건지 -할건지 가지쳐나감.

마지막 숫자까지 탐색해야만 target값과 일치하는지 확인가능하므로 prunding불가.

target값과 일치하는 가지의 수를 구해야하므로 탐색하는 함수 바깥에 변수를 선언해야만 함수의 동작 횟수를 알 수 있음.
class같은 경우 메소드를 통해  attribute값을 증가시키는 것이 가능하지만 프로그래머스에서 함수로 주어지므로
nonlocal로써 이전 함수의 변수를 참조하도록 설정.


numbers를 pop하며 탐색하려고 했지만 OS강의에서 pointer에 대한 내용, file읽는 방식떠올려보니 굳이 그럴 필요 없음.
따라서 index를 증가시키면서(pointer??) 해당 값만 복사해서 가져온다. 원형은 건드리지 말어.(메모리 share 생각~!)
'''
def solution(numbers, target):
    answer = 0
    
    def FindTarget(numbers, i, target, value):
        nonlocal answer
        if i == len(numbers):
            if value == target:
                answer += 1
            return
        
        num = numbers[i]
        FindTarget(numbers,i+1,target,value-num)
        FindTarget(numbers,i+1,target,value+num)
    
    FindTarget(numbers,0,target,0)
    return answer
