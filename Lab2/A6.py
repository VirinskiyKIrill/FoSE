s = int(input())
m = 0
h = 0
while s >= 60:
    s -= 60
    m += 1
while m >= 60:
    m -= 60
    h += 1
while h >= 24:
    h = 0
print('{}:{:02}:{:02}'.format (h,m,s))