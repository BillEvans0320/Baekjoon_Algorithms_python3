
A = int(input())
B = int(input())
C = int(input())

ABC = A*B*C

string_ABC = str(ABC)


for i in range(10):
    count_num = string_ABC.count(str(i))
    print(count_num)
