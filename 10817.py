# When Three integers are given: A, B and C,
# write a program that prints the second largest integer.

A, B, C = list(map(int,input().split()))

if A >= B:
    if A <= C:
        print(A)
    elif B >= C:
        print(B)
    else:
        print(C)
else:
    if A >= C:
        print(A)
    elif B <= C:
        print(B)
    else:
        print(C)

"""
using "sorted" function

numbers = map(int,input().split())
arranged_numbers = sorted(numbers, reverse=True)
print(arranged_numbers[1])

"""
