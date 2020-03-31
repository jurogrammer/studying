def solution(board, moves):
    n = len(board)
    tops = [0 for _ in range(n)] #값이 있는 index

    for c in range(n):
        for r in range(n):
            if board[r][c] != 0:
                tops[c] = r
                break

    answer = 0
    basket = []
    for m in moves:
        position = m-1 #꺼낼 장소
        top = tops[position] #꺼낼 장소에 있는 top 번호
        if top == n: #비어 있으면 다음으로
            continue
        tops[position]+=1 #꺼낸 장소에 있는 top 1 감소

        item = board[top][position]  # 꺼낸 아이템
        if not basket: #배스킷 비어 있으면
            basket.append(item)
        else:
            if basket[-1] == item:
                basket.pop()
                answer += 2
            else:
                basket.append(item)

    return answer