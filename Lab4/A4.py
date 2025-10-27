import string
import re


def valid_code(code):
    t_f = code.isdigit() and len(code) in [13, 15, 16]
    return t_f


def check_sum(num):
    check = 0
    for i in range(len(num) - 2, - 1, -2):
        doubled = int(num[i]) * 2
        if doubled > 9:
            doubled -= 9
        check += doubled
    for i in range(len(num) - 1, -1, -2):
        check += int(num[i])
    return check


def card_type(num):
    if (len(num) == 13 or len(num) == 16) and num.startswith("4"):
        return "Visa"
    if len(num) == 15 and num.startswith("37"):
        return "American Express"
    if len(num) == 16 and re.match(r'5[1-5]', num[:2]):
        return "Master Card"
    return "Invalid"


card = input("Enter number: ")
if valid_code(card):
    if check_sum(card) % 10 == 0:
        print(card_type(card))
    else:
       print("Invalid")
