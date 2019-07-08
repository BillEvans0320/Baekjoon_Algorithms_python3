# write a program printing a multiplication table for 'N' after entering a number 'N'

N = int(input())

for i in range(9):
    print("%d * %d = %d"%(N,i+1,N*(i+1)))
