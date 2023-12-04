total = 0
with open('../input/day01.txt', encoding='utf-8') as input:
    for line in input:
        for char in line:
            if char.isdigit():
                total += (int(char)*10)
                break
        for char in reversed(line):
            if char.isdigit():
                total += int(char)
                break

print(total)