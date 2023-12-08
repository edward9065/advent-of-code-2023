instructions = ""
network = {}
current_node = "AAA"
with open("../input/day08.txt", encoding="utf-8") as input:
    for i, line in enumerate(input):
        if i > 1 :
            network[line[0:3]] = (line[7:10], line[12:15])
        elif i == 0:
            instructions = line

count = 0

while(current_node != "ZZZ"):
    direction = instructions[count % ((len(instructions)-1))]
    count += 1
    if direction == "R":
        current_node = network[current_node][1]
    else:
        current_node = network[current_node][0]
    

print(count)