def solution(arrangement):
    stack = []
    answer = 0

    counts = 0
    flag = False #레이저 만나서 pop했었니? 에 대한 플래그
    for token in arrangement:
        if token == '(':
            stack.append(token)
            flag = False
        else:
            stack.pop()
            if flag:
                answer += 1
            else:
                answer += len(stack)
            flag = True

    return answer

arrangement= "()(((()())(())()))(())"

print(solution(arrangement))