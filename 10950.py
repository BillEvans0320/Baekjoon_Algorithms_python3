# write a program to print A+B after entering integer 'A' and 'B'

T = int(input())

for i in range(T):
    A, B = list(map(int,input().split()))
    print(A+B)
