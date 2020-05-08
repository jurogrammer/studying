numMapped = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
             10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def convertDecimalNum(number,n):
    convertedNum = ''
    while n<=number:
        convertedNum += numMapped[number%n]
        number = number//n
    convertedNum += numMapped[number]

    convertedNum = list(convertedNum)
    convertedNum.reverse()
    convertedNum = "".join(convertedNum)
    return convertedNum


def solution(n, t, m, p):
    listToSpeak = ''

    # 50000이란 숫자는 숫자 몇까지 세야할 지 모르기 때문에. 최적화하려면 계산.
    for number in range(50000):
        listToSpeak += convertDecimalNum(number,n)

    i = 0
    answer = ''
    while i<t:
        answer += listToSpeak[p+i*m - 1]
        i += 1

    return answer