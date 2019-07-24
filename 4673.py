# key point : self number, if i in list:


def check_self_number(n = int):
    part_sum = 0
    str_n = str(n)
    for i in range(len(str_n)):
       part_sum += int(str_n[i])

    no_self_number = n + part_sum
    return no_self_number

def main():
    upper_range = 10000
    no_self_number_list = []
    for n in range(1,upper_range+1):
        no_self_number_list.append(check_self_number(n))

    for i in range(1,upper_range+1):
        if i in no_self_number_list:
            continue
        else:
            print(i)

if __name__ == "__main__":
    main()
