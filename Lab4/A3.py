import string
from statistics import quantiles

print("Enter string (1/0)")
packets = input()
num_pack = len(packets)
if not all(char in '01' for char in packets):
    print("Input error")
num_loss = packets.count('0')
max_loss_streak = 0
current_loss_streak = 0
for packet in packets:
    if packet == '0':
        current_loss_streak += 1
        max_loss_streak = max(max_loss_streak, current_loss_streak)
    else:
        current_loss_streak = 0
loss_percent = (num_loss / num_pack) * 100
if loss_percent <= 1:
    quality = "Excellent quality"
elif loss_percent <= 5:
    quality = "Good quality"
elif loss_percent <= 10:
    quality = "Bad quality"
else:
    quality = "Critical network quality"
print(f"Total number of packets: {num_pack}")
print(f"Number of lost packets: {num_loss}")
print(f"Length of longest sequence of lost packets: {max_loss_streak}")
print(f"Loss percentage: {loss_percent:.1f}%")
print(f"Network quality: {quality}")