# Key word : repeated string


case = int(input())

for i in range(case):
    num, words = input().split()

    num = int(num)

    num_words = ''
    for word in words:
        num_words += word*num
    print(num_words)

'''
#first version

case = int(input())

for i in range(case):
    num, string = input().split()

    num = int(num)

    for i in range(len(string)):
        for j in range(num):
            print(string[i],end='')
    print("")
'''
