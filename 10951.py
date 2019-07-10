# print 'A + B', using 'while'
import sys

while True:
    A, B = list(map(int, sys.stdin.readline().split()))
    print(A+B)
