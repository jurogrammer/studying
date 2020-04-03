def solution(dartResult):
    stage = 0
    scores = [0,0,0,0]
    nums = {'0','1','2','3','4','5','6','7','8','9'}
    SDT = {'S','D','T'}

    i = 0
    n = len(dartResult)

    while i < n:
        val = dartResult[i]
        if val in nums:
            stage += 1
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                i += 1
                scores[stage] = 10
            else:
                scores[stage] = int(dartResult[i])
        elif val in SDT:
            if val == 'D':
                scores[stage] = pow(scores[stage],2)
            elif val == 'T':
                scores[stage] = pow(scores[stage],3)
        else:
            if val == '*':
                scores[stage-1]*=2
                scores[stage]*=2
            else:
                scores[stage] = -scores[stage]
        i += 1



    answer = sum(scores)
    return answer

dartResult = '1S2D*3T'
print(solution(dartResult))


