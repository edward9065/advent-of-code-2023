import math

with open('../input/day06.txt', encoding='utf-8') as input:
    data = input.read().split("\n")

times = [int(x) for x in data[0].split()[1:]]
distances = [int(x) for x in data[1].split()[1:]]

product = 1

for i in range(len(times)):
    first_winning_time = int((-times[i] + math.sqrt(times[i]**2 - (-4*(-distances[i])))) / -2) + 1
    second_winning_time = min(times[i], times[i] - first_winning_time)
    product *= (second_winning_time - first_winning_time + 1)

print(product)