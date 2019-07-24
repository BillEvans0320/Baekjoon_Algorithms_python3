# Key word : star, fractal, Divide and Conquer
import sys

def print_star(N,i,j):

    if i % 3 == 1 and j % 3 == 1:
        sys.stdout.write(" ")
        return
    else:
        if N//3 == 0:
            sys.stdout.write("*")
        else:
            print_star(N//3,i//3,j//3)
    return


def main():
    N = int(sys.stdin.readline())

    for i in range(N):
        for j in range(N):
            print_star(N,i,j)

        sys.stdout.write("\n")
    return


if __name__ == "__main__":
    main()

'''
# 컴파일 시간 초과로 인한 다른 답

import sys

num = int(input())

def star(i, j):
    while(i != 0):
        # 몫이 1인 경우
        if(i % 3 == 1 and j % 3 == 1):
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        i = i // 3
        j = j // 3
    sys.stdout.write('*')

for i in range(num):
    for j in range(num):
            star(i, j)
    sys.stdout.write('\n')

    출처 : https://hwiyong.tistory.com/213
'''
