# make a program printing a alarm time

H, M = input().split()

H = int(H)
M = int(M)

alarm = H * 60 + M - 45

if alarm < 0:
    alarm = 24 * 60 + M - 45

alarm_H = alarm // 60
alarm_M = alarm % 60

print(alarm_H, alarm_M)
