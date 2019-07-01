# makge a program to discriminate whether leap year

year = int(input())

if (year % 4) == 0:
    if (year % 400) != 0 and (year % 100) == 0:
        print("0")
    else:
        print("1")
else:
    print("0")

"""
# other solution

year = int(input())

if((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)):
    print('1')
else:
    print('0')

source : https://hwiyong.tistory.com/202
"""
