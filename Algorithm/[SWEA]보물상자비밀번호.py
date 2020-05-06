testCase = int(input())

stringToNums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def putOxNumber(treasureBox,sideLength,oxNumbersSet):
        for i in range(4):
            oxNumbersSet.add(treasureBox[i*sideLength : (i+1)*sideLength])

def rotate(treasureBox):
    return treasureBox[-1] + treasureBox[:-1]

def convertOxToDecimal(oxNum,sideLength):
    decimalNum = 0
    for i in range(sideLength):
        decimalNum += pow(16,i)*stringToNums[oxNum[-1*(i+1)]]

    return decimalNum

for test in range(1,testCase+1):
    n,k = map(int,input().split())
    treasureBox = input()

    sideLength = n//4
    oxNumbersSet = set()

    for _ in range(sideLength):
        treasureBox = rotate(treasureBox)
        putOxNumber(treasureBox,sideLength,oxNumbersSet)

    numList = []
    for oxNum in oxNumbersSet:
        numList.append(convertOxToDecimal(oxNum,sideLength))

    numList.sort(reverse=True)

    rst = numList[k-1]
    print("#{} {}".format(test,rst))