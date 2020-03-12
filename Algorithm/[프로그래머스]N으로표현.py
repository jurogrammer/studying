cnt_min = 9

def DFS(N, rst, cnt, number):
    global cnt_min
    if rst == number:
        if cnt < cnt_min:
            cnt_min = cnt
            return

    for i in range(1, 9 - cnt):
        n_opr = int(N * i)
        DFS(N, rst + n_opr, cnt + i, number)
        DFS(N, rst - n_opr, cnt + i, number)
        DFS(N, rst * n_opr, cnt + i, number)
        DFS(N, rst // n_opr, cnt + i, number)

def solution(N, number):
    DFS(str(N), 0, 0, number)
    if cnt_min > 8:
        answer = -1
    else:
        answer = cnt_min

    return answer
