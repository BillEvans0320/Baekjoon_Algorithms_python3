# make a program printing a alarm time

H, M = input().split()

H = int(H)
M = int(M)

if M >= 45:
    print(H, M-45)
else:
    if H == 0:
        print(23, M+15)
    else:
        print(H-1, M+15)
