def input_grade(num_subject):
    score = list(range(num_subject))

    for i in range(1,num_subject+1):
        score[i-1] = int(input("%d번째 과목의 점수를 입력하세요 : "%i))
    return score

def get_average_score(score):
    total_score = 0
    for i in range(len(score)):
        total_score += score[i]
    avg_score = total_score / len(score)
    print("평균 점수 : ",avg_score)
    return avg_score

def output_grade(avg_score):

    if avg_score >= 90:
        grade = 'A'
    elif avg_score >= 80:
        grade = 'B'
    elif avg_score >= 70:
        grade = 'C'
    elif avg_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("학점 : ",grade)
    return grade

print("Start of Exam Grader Program")
print("============================")

num_subject = int(input("과목수를 입력하세요 : "))

score = input_grade(num_subject)
avg_score = get_average_score(score)
grade = output_grade(avg_score)

print("============================")
print("End of Exam Grader Program")
