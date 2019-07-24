# key point : set
# 1 ~ 9
# 10 ~ 99
# 100 : 1 0 0 (x)
# 101 : 1 0 1 (x)
# 123 : 1 2 3 (O)


def check_arithmetic(N = int):
    str_N = str(N)
    arithmetic_list = [0]*(len(str_N)-1)

    for i in range(len(str_N)-1):
        arithmetic_list[i] = int(str_N[i+1]) - int(str_N[i])

    set_arithmeetic_list = set(arithmetic_list)

    if len(set_arithmeetic_list) <= 1:
        check_cnt = 1
    elif len(set_arithmeetic_list) >= 2:
        check_cnt = 0

    return check_cnt


def main():
    N = int(input())
    total = 0

    for i in range(N):
        total += check_arithmetic(i+1)

    print(total)
    return


if __name__ == "__main__":
    main()
