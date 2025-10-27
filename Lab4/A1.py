import random
import time
all_time = 0
right_answers = 0
n = int(input())
for i in range(n):
    print(f"Question {i}/{n}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    right_answer = a * b
    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} * {b} = "))
            time_spend = time.time() - start_time
            break
        except ValueError:
            print("input error")
    if answer == right_answer:
        print("Right!")
        print(f"(Time: {time_spend})")
        right_answers += 1
    else:
        print("Wrong!")
        print(f"Right: {right_answer} (Time: {time_spend})")
    all_time += time_spend
print("==============================================")
print("STATISTICS")
print("==============================================")
print(f"General time: {all_time}")
average_time = all_time / n
print(f"Average time per question : {average_time}")
print(f"Right answers: {right_answers}/{n}")
percent = right_answers / n * 100
print(f"Percentage of right answers: {percent}%")

