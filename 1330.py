# when both A and B are inserted, make a program for comparing A with B

A, B = input().split()

A = int(A)
B = int(B)

if (A > B):
    print(">")
elif (A < B):
    print("<")
else:
    print("==")
