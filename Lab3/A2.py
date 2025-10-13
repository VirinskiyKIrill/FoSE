password = input()
import string
spec = '#-*'
allowed = string.ascii_uppercase + string.ascii_lowercase +string.digits + spec
len(password)
if len(password) != 8:
    print("Password length is not 8")
if password.lower() == password:
    print("There are no capital letters in the password")
if password.upper() == password:
    print("There are no lowercase letters in the password")
if False == any(symbol.isdigit() for symbol in password):
    print("There are no numbers in the password")
if False == any(symbol in spec for symbol in password):
    print("There are no special symbols in the password")
if False == any(symbol in allowed for symbol in password):
    print("The password uses unexpected symbols")



