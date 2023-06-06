#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
compare = abs(number) % 10
str = ""
if compare > 5 :
    str = "and is greater than 5"
elif compare == 0 :
    str = "and is 0"
elif compare < 6 and compare != 0:
    str = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {compare:d} {str:s}")
