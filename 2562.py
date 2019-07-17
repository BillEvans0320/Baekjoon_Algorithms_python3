# print a maximum value on the first line and its position on the second line

numbers = [0]*9
for i in range(9):
    numbers[i] = int(input())

print(max(numbers))
print(numbers.index(max(numbers))+1)
