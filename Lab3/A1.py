x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
def chet(x, y):
    if ((x > 0) and (y > 0)):
        return 1
    elif ((x < 0) and (y > 0)):
        return 2
    elif ((x < 0) and (y < 0)):
        return 3
    elif ((x > 0) and (y < 0)):
        return 4
    else:
        print("input error")
if chet(x1,y1) == chet(x2, y2):
    print("Yes \n")
    print(chet(x1, y1))
else:
    print("No")