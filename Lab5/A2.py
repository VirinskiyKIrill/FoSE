import re
import string
let = string.ascii_lowercase + string.ascii_uppercase
print("Enter the text")
text = input()
l_sent = re.split(r'(?<=[.?!])', text)
i = len(l_sent) - 1
for j in range(i):
    print(l_sent[j].strip())
print(f"The number of strings: {i}")