def solution(prices):
    stack = [] #element : (price, index(day))
    n = len(prices)
    answer = [0] * n
    for curDay in range(n):
        curStockPrice = prices[curDay]

        while stack:
            preStockPrice, preDay = stack.pop()
            #현재 값이 더 크다면 넘겨!
            if curStockPrice >= preStockPrice:
                stack.append((preStockPrice,preDay))
                break
            answer[preDay] = curDay-preDay

        stack.append((curStockPrice,curDay))

    #마지막날 정산
    while stack:
        preStockPrice, preDay = stack.pop()
        answer[preDay] = curDay-preDay

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))