# write a program printing sum of A and B after entering A and B

test_case = int(input())

for i in range(test_case):
    A, B = list(map(int, input().split()))
    print("Case #%d: %d"%(i+1,A+B))
