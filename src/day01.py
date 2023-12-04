import re

total = 0

words2digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}

with open('../input/day01.txt', encoding='utf-8') as input:
    for line in input:
        pattern = re.compile(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))')
        matches = pattern.findall(line)
        total += (10*words2digits[matches[0]] + words2digits[matches[-1]])
        
print(total)