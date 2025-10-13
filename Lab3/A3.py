pr = int(input())
now = int(input())
used = now - pr
if used <= 300:
    pay = 21
elif used <= 600:
    pay = 21 + (used - 300) * 0.06
elif used <= 800:
    pay = 21 + 300 * 0.06 + (used - 600) * 0.04
elif used > 800:
    pay = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
else:
    print("input error")
av = pay / used
print(f"Previous: {pr}")
print(f"Current: {now}")
print(f"Used: {used}")
print(f"For payment: {pay:.2f}")
print(f"Av.price m^3: {av:.2f}")


