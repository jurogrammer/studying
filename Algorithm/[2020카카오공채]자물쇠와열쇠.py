def rotate(r, c, M):
    pr = (M - 1) / 2
    pc = (M - 1) / 2
    return int(-c + pc + pr), int(r - pr + pc)

def rotatePoints(points,M):
    rotatedPoints = set()
    for r,c in points:
        rotatedR,rotatedC = rotate(r,c,M)
        rotatedPoints.add((rotatedR,rotatedC))
    return rotatedPoints

def check(keyDolgis,lockHomes,lockDolgis):
    for lockDolgi in lockDolgis:
        if lockDolgi in keyDolgis:
            return False

    for lockHome in lockHomes:
        if lockHome not in keyDolgis:
            return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    keyDolgis = set()
    for c in range(m):
        for r in range(m):
            if key[r][c] == 1:
             keyDolgis.add((r,c))
    lockDolgis = set()
    lockHomes = set()
    for c in range(n):
        for r in range(n):
            if lock[r][c] == 1:
                lockDolgis.add((r,c))
            else:
                lockHomes.add((r,c))

    answer = False
    for _ in range(4):
        keyDolgis = rotatePoints(keyDolgis,m)
        for dr in range(-m+1,m+n-1):
            for dc in range(-m+1,m+n-1):
                movedKeyDolgis = set()
                for kr,kc in keyDolgis:
                    movedKeyDolgis.add((kr+dr,kc+dc))
                isOpen = check(movedKeyDolgis,lockHomes,lockDolgis)
                if isOpen is True:
                    answer = True
                    return answer

    return answer