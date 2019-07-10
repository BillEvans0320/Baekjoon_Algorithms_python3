# write a program printing a lenth of 'N' cycle when 'N' is entered.
import sys

A = int(sys.stdin.readline())

new_num = A
cycle = 1

while True:
    tens_num = new_num // 10
    units_num = new_num % 10
    tens_units_sum = tens_num + units_num
    new_num = units_num*10 + tens_units_sum % 10

    if A == new_num:
        print(cycle)
        break
    else:
        cycle += 1
        continue
