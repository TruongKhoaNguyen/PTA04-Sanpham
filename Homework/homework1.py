time = list(map(int,input().split(":")))
hople = 0
if time[0] >= 0 and time[0] <= 23:
    hople += 1
if time[1] >= 0 and time[1] <= 59:
    hople += 1
if time[2] >= 0 and time[2] <= 59:
    hople += 1
if hople >= 3:
    print("Hợp lệ!")
else:
    print("Không hợp lệ!")