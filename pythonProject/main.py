hours = 0
minutes = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        hours += 1
    elif x < 0 and y > 0:
        hours += 10
    elif x < 0 and y < 0:
        minutes += 10
    else:
        minutes += 1
if 23 >= hours >= 0 and 59 >= minutes >= 0:
    print(("0" + str(hours))[-2:], ("0" + str(minutes))[-2:], sep=":")
else:
    print("Clock is broken")
