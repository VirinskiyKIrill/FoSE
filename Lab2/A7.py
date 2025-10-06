a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a % b == 0) and (c % b == 0)):
    print("YES")
    print("White")
elif ((a % b == 1) and (c % b == 1)):
    print("YES")
    print("Black")
else:
    print("NO")