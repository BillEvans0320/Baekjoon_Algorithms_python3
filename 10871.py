# print a entered number which is less than 'X', separated by spaces.
# there is at least one number smaller than X at least
import sys

N, X = list(map(int, sys.stdin.readline().split()))
list_N = list(map(int, sys.stdin.readline().split()))
# list_N is list type which have inserted integer of N numbsers

for i in range(N):
    if (list_N[i] < X):
        print(list_N[i],end=' ')
    else:
        continue
