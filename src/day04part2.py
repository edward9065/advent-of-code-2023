with open("../input/day04.txt", encoding="utf-8") as input:
    card_copies = [1]

    for index, line in enumerate(input):
        line_data = line.split(":")[1].split("|")
        winning_set = set(line_data[0].split())
        
        ticket_numbers = line_data[1].split()
        count = sum(1 for num in ticket_numbers if num in winning_set)
        if len(card_copies) < index+1:
            card_copies.append(1)
        if count > 0:
            for i in range(index+1, index+count+1):
                if len(card_copies) <= i:
                    card_copies.append(1+card_copies[index])
                else: 
                    card_copies[i] += card_copies[index]
         
        
print(sum(card_copies))