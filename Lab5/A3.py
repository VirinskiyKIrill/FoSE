text = input().strip()
words = text.split()

abreviation = []
for word in words:
    if len(word) >= 3:
        abreviation.append(word[0].upper())
result = ''.join(abreviation)
print(result)