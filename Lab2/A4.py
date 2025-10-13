a = int(input())
b = int(input())
if 1 > (a or b) > 1000:
    result = [a, b][a <= b]
    print(result)
else:
    print("The numbers are not included in the range")