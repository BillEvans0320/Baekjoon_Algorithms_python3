# Hanoi Tower
# Key word : recursive function


def move_plate(x,y,plate_num):
    if plate_num == 0:
        return
    move_plate(x,6-x-y,plate_num-1)         # 원반-1 개의 원반을 기둥 1에서 기둥2로 옮긴다.
    print(x,y)                              # 옮긴 후, 기둥 1에서의 원반을 3으로 옮긴다.
    move_plate(6-x-y,y,plate_num-1)         # 기둥 2에서 3으로 원반을 옮긴다.
    return


def main():
    plate_num = int(input())

    total_cnt = (2**plate_num) - 1
    print(total_cnt)

    move_plate(1,3,plate_num)
    return


if __name__ == "__main__":
    main()
