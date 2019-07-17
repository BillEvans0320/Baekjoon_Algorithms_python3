# write a program to find the maximum and minimum value when 'N' integers are given

import sys

N = int(input())
integers = list(map(int, sys.stdin.readline().split()))

sorted_integers = sorted(integers)
print(sorted_integers[0],sorted_integers[N-1])
