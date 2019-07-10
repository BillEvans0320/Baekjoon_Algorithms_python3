# print 'A + B', using 'while'
import sys

A, B = list(map(int, sys.stdin.readline().split()))
while A != 0 and B != 0:
    print(A+B)
    A, B = list(map(int, sys.stdin.readline().split()))

"""
another code

while(True):
    A, B = list(map(int, input().split()))
    if(A == 0 and B == 0):
        break
    else:
        print(A + B)

https://hwiyong.tistory.com/m/207?category=844316
"""
