convert = {'C':'C', 'C#':'Z', 'D':'D', 'D#':'X', 'E':'E', 'F':'F', 'F#':'N', 'G':'G', 'G#':'J', 'A':'A', 'A#':'L', 'B':'B', 'E#':'K'}

def convertTime(time):
    h,m = time.split(":")

    return int(m)+int(h)*60

def convertSM(stringSheetMusic):
    sheetMusic = []
    sheetNum = -1
    for token in stringSheetMusic:
        if token == "#":
            sheetMusic[sheetNum] += token
        else:
            sheetMusic.append(token)
            sheetNum += 1
    n = len(sheetMusic)
    for i in range(n):
        sheetMusic[i] = convert[sheetMusic[i]]

    return sheetMusic

def solution(m, musicinfos):
    result = []
    m = "".join(convertSM(m))

    for musicinfo in musicinfos:
        stringStart,stringEnd,title,stringSheet = musicinfo.split(",")
        start = convertTime(stringStart)
        end = convertTime(stringEnd)
        sheet = convertSM(stringSheet)
        sheetNum = len(sheet)

        rep = (end-start)//sheetNum
        remain = (end-start)%sheetNum

        csdSheet = sheet*rep + sheet[:remain]
        csdSheet = "".join(csdSheet)

        if csdSheet.find(m) != -1:
            result.append((end-start,start,title))

    answer = ''

    if result :
        result.sort(key = lambda a : (-a[0],a[1],a[2]))
        answer = result[0][2]

    else:
        answer = "(None)"

    return answer


#
#
# import random
# m_legnth = 4
# m = ''
#
# sheet = ''
# sheet_length = 10
#
# mapped = {1:"C", 2:"C#", 3:"D", 4:"D#", 5:"E", 6:"F", 7:"F#", 8:"G", 9:"G#", 10:"A", 11:"A#",12:'B'}
#
# rep  = 10000
# for _ in range(rep):
#     for _ in range(m_legnth):
#         m += mapped[random.randint(1,12)]
#
#     start = random.randint(1,49)
#     end = start+sheet_length
#
#
#     for _ in range(sheet_length):
#         sheet += mapped[random.randint(1,12)]
#
#     musicinfos = ["12:"+str(start)+","+"12:"+str(end)+","+"hihihi,"+sheet]
#
#     try :
#         solution(m,musicinfos)
#     except:
#         print(m)
#         print(musicinfos)
