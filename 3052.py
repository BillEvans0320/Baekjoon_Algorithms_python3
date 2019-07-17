list_num = []

for i in range(10):
    num = int(input())
    list_num.append(num%42)

set_list_num = set(list_num)
print(len(set_list_num))
