subject_num = int(input())

score = [0]*subject_num
score = list(map(int,input().split()))

max_score = max(score)

new_score = [0]*subject_num
for i in range(subject_num):
    new_score[i] = score[i]/max_score*100

score_avg = sum(new_score) / subject_num
print(score_avg)
