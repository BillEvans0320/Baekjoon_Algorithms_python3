# third decimal place


test_case = int(input())

for i in range(test_case):
    test_score = list(map(int, input().split()))

    score_avg = sum(test_score[1:])/test_score[0]
    avg_ex_student = 0

    for j in range(1,len(test_score)):
        if test_score[j] > score_avg:
            avg_ex_student += 1

    print("%.3f%%"%round(avg_ex_student/test_score[0]*100,3))
