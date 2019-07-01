"""
make a program that showing numbers
when two Three-digit natural numbers are multipied
"""
"""
for example,
input : 472, 385
output : 2360, 3776, 1416, 181720
"""

A = int(input())
B = input()

B = list(B) # B[0],B[1],B[2]
first_answer = A * int(B[2])
second_answer = A * int(B[1])
third_answer = A * int(B[0])
final_answer = first_answer + 10 * second_answer + 100 * third_answer

print(first_answer)
print(second_answer)
print(third_answer)
print(final_answer)


""" 
Another solution

a = int(input())
b = int(input())
print("%d\n%d\n%d\n%d"%((a * (b % 10)), (a * ((b % 100)//10)), (a * (b//100)), (a * b)))
"""
