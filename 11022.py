# write a program printing A, B and sum of A and B after entering A and B
import sys
test_case = int(input())

for i in range(test_case):
    A, B = list(map(int, sys.stdin.readline().split()))
    print("Case #%d: %d + %d = %d"%(i+1,A,B,A+B))
