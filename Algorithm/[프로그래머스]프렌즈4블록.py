def check(board,x1,x2,x3,x4,y1,y2,y3,y4):
    if board[y1][x1] != '#' and board[y1][x1] == board[y2][x2] and \
        board[y1][x1] == board[y3][x3] and board[y1][x1] == board[y4][x4]:
        return True
    else:
        return False

def arrangeCol(board,m,c):
    stack = []
    emptyCnt = 0
    for r in range(m-1,-1,-1):
        if board[r][c] != '#':
            stack.append(board[r][c])
        else:
            emptyCnt += 1

    for _ in range(emptyCnt):
        stack.append('#')

    for r in range(m):
        board[r][c] = stack.pop()

def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    answer = 0
    while True:
        delList = set()
        for r in range(m-1):
            for c in range(n-1):
                y1,x1 = r,c
                y2,x2 = r+1,c
                y3,x3 = r,c+1
                y4,x4 = r+1,c+1
                if check(board,x1,x2,x3,x4,y1,y2,y3,y4):
                    delList.add((y1,x1))
                    delList.add((y2,x2))
                    delList.add((y3,x3))
                    delList.add((y4,x4))
        if not delList:
            break
        answer += len(delList)

        for delR,delC in delList:
            board[delR][delC] = '#'

        for c in range(n):
            arrangeCol(board,m,c)

    return answer #delList 다 등록후 그 길이만큼 answer에 더하자.
'''
'CCBDE'
'AAADE'
'AAABF'
'CCBBF'
'''
m = 4
n = 5
board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
print(solution(m,n,board))