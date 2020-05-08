dict = {}
for i in range(65,65+26):
    dict[str(chr(i))] = i-65+1

def solution(msg):
    answer = []
    i = 0
    maxIdx = 26
    msgLength = len(msg)
    while i<msgLength:
        letter = msg[i]
        while letter in dict:
            i += 1
            if i>=msgLength:
                break
            letter+=msg[i]

        if i != msgLength:
            maxIdx += 1
            dict[letter] = maxIdx
        if i != msgLength:
            answer.append(dict[letter[:-1]])
        else:
            answer.append(dict[letter])


    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))