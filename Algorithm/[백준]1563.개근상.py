'''
O L A1 A2
1일
1 1 1 0

결석 A1 A2선언
2일
sum(O,L,A1,A2), sum(O,A1,A2), sum(O,L,A1,A2)

3일
sum(O,L,A1,A2), sum(O,A1,A2), sum(O,L,(O+L),A1)

'''

n = int(input())

O = 1
L = 1
A1 = 1
A2 = 0


for _ in range(n):
    O,L,A1,A2 = O+L+A1+A2,O+A1+A2,L,A1
print(O+L+A1+A2)