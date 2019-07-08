# write a program to print A+B after entering integer 'A' and 'B'
import sys

T = int(input())

for i in range(T):
    A, B = list(map(int,sys.stdin.readline().split()))
    print(A+B)
