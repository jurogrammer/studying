def sol(n,inputList):
    def pop(M, F):  # 사용물건에 대한 pop
        mail.pop(M)
        femail.pop(F)


    string = ''
    inputM = 0
    inputF = 1
    i = 0
    mail = {}
    femail = {}  # index : femail val : mail
    for M,F in inputList:
        mail[M] = F
        femail[F] = M

    pop(M, F)

    string += (str(M) + ' ' + str(F))
    ''' dict엔 암-수 수-암 각 파트로 들어있음. 그래서 수에 대한 암이 존재하는지 알아야함. M암 F수'''
    for _ in range(n - 1):
        if M in femail:  # 수-암에서 수와 맞는 new암이 있느냐 M과 F는 최상단.
            newF = M
            newM = femail[newF]
            string = (str(newM) + ' ' + str(newF) + ' ') + string
            pop(newM, newF)
            M = newM

        if F in mail:  # 수-암에서 암과 맞는 new수가 있느냐?

            newM = F
            newF = mail[newM]
            string = string + (' ' + str(newM) + ' ' + str(newF))
            pop(newM, newF)
            F = newF
    return string

def makeArray(table,n): #-1 visited 0 : nothing  0< <10:bad
    totalArray = []
    for r in range(n):
        for c in range(n):
            if table[r][c]>0:
                i,j = r,c

                while i<n and j<n:
                    if table[i][j] > 0:
                        j += 1
                    else: break
                j -= 1

                while i<n and j<n:
                    if table[i][j] > 0:
                        i += 1
                    else : break
                i -= 1

                totalArray.append((i-r+1,j-c+1))
                for l in range(r,i+1):
                    for m in range(c,j+1):
                        table[l][m] = -1
    return totalArray

def matrixChain(n,p):

    return m[1][n]

testCase = int(input())
for t in range(1,testCase+1):
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(n)]
    arrayList = makeArray(table,n)
    print(arrayList)
    p = list(map(int,sol(n,arrayList).split(" ")))
    arrayN = len(arrayList)
    print(matrixChain(arrayN,p))