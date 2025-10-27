print("Choose one of three shapes")
print("1.Rectangle 2.Triangle 3.Frame")
choose = int(input())
print("Enter symbol")
sym = input()
def rectangle(sym):
    print("Enter length and height(lxh)")
    length = int(input())
    height = int(input())
    for i in range(height):
        for j in range(length):
            print(sym, end ="")
        print("")

def triangle(sym):
    print("Enter size")
    size = int(input())
    a = sym
    for i in range(size):
        print(a)
        a += sym
def frame(sym):
    print("Enter length and height(lxh)")
    length = int(input())
    height = int(input())
    for i in range(height):
        for j in range(length):
            if (0 < j < (length - 1)) and (0 < i < (height - 1)):
                print(" ", end = "")
            else:
                print(sym, end = "")
        print("")
if choose == 1:
    rectangle(sym)
elif choose == 2:
    triangle(sym)
elif choose == 3:
    frame(sym)
else:
    print("Input error")