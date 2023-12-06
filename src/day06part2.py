import math

with open('../input/day06.txt', encoding='utf-8') as input:
    data = input.read().split("\n")

time = int("".join(data[0].split()[1:]))
distance = int("".join(data[1].split()[1:]))

first_winning_time = int((-time + math.sqrt(time**2 - (-4*(-distance)))) / -2) + 1
second_winning_time = min(time, time - first_winning_time)

print(second_winning_time - first_winning_time + 1)