from functools import reduce 

instructions = ""
network = {}
nodes_ending_in_A = []
with open("../input/day08.txt", encoding="utf-8") as input:
    for i, line in enumerate(input):
        if i > 1 :
            network[line[0:3]] = (line[7:10], line[12:15])
            if line[2] == "A":
                nodes_ending_in_A.append(line[0:3])
        elif i == 0:
            instructions = line

multiples = []
for current_node in nodes_ending_in_A:
    count = 0

    while(current_node[2] != "Z"):
        direction = instructions[count % ((len(instructions)-1))]
        count += 1
        if direction == "R":
            current_node = network[current_node][1]
        else:
            current_node = network[current_node][0]
        

    multiples.append(count)

def get_GCD(a: int, b: int):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return get_GCD(b, a%b)
    
def get_GCD_from_list(numbers: list) -> int:
    gcd = get_GCD(numbers[0], numbers[1])
    for num in numbers[2:]:
        gcd = get_GCD(gcd, num)
    return gcd

gcd = get_GCD_from_list(multiples)

# if it's not a .0, we have an error, so I didn't use // instead of /
multiples = [x/gcd for x in multiples]

print(reduce(lambda x, y: x*y, multiples) * gcd)