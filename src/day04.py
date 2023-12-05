total = 0
with open("../input/day04.txt", encoding="utf-8") as input:
    for line in input:
        line_data = line.split(":")[1].split("|")
        winning_set = set(line_data[0].split())
        
        ticket_numbers = line_data[1].split()
        count = sum(1 for num in ticket_numbers if num in winning_set)
        total += int(2**(count-1))
        
print(total)