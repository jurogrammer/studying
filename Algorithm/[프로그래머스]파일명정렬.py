def getHeadNumber(file):
    string = ''
    number = ''
    fileLength = len(file)
    i = 0
    while file[i].isalpha() or file[i] == ' ' or file[i] == '.' or file[i] =='-':
        if file[i].isalpha():
            string += file[i].lower()
        else:
            string += file[i]
        i += 1

    cnt = 5
    while i<fileLength and cnt != 0 and file[i].isnumeric():
        number += file[i]
        cnt -= 1
        i += 1

    return string,int(number)

def solution(files):
    splitedElems = []
    for idx,file in enumerate(files):
        head,number = getHeadNumber(file)
        splitedElems.append((head,number,idx,file))

    answer = []
    splitedElems.sort(key = lambda a : (a[0],a[1],a[2],a[3]))
    filesLength = len(files)
    for element in splitedElems:
        answer.append(element[3])

    return answer

files = 	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))