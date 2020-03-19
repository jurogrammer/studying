
n = int(input())
buildings = [0]+list(map(int,input().split()))
stack = []

for i in range(1,n+1):
    h = buildings[i]
    if stack:
        empty = False
    else:
        stack.append((i,h))
        print(0, end=" ")
        continue

    while stack[-1][1] < h :
        if stack:
            stack.pop()
            if not stack:
                empty = True
                break

    if empty :
        print(0, end=" ")
    else:
        print(stack[-1][0], end=" ")
    stack.append((i,h))

