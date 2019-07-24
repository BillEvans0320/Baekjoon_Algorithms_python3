# key idea : split('X'), total_sum += (n * (n+1)) // 2


import sys

quiz_result_num = int(sys.stdin.readline())

for i in range(quiz_result_num):
    quiz_result = input()

    split_X = quiz_result.split('X')
    total_score = 0

    for i in split_X:
        score = len(i)

        if score >= 1:
            total_score += (score*(score+1))//2

    print(total_score)
