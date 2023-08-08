#!/usr/bin/python3

for num in range(100):
    formatted_num = f"{num:02}"
    if num == 89:
        print(formatted_num)
    else:
        num2 = str(num % 10)
        num2 += str(num // 10)
        if num > int(num2) or num % 11 == 0:
            continue
        print(formatted_num, end=", ")
