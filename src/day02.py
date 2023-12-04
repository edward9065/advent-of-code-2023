cube_count = {
    "red": 12,
    "green": 13,
    "blue": 14,
    "red\n": 12,
    "green\n": 13,
    "blue\n": 14,
}
# doing red\n is faster than stripping the string, for the cost of negligible space

total = 0

with open('../input/day02.txt', encoding='utf-8') as input:
    for line in input:
        game_data = line.split(": ")
        draws = game_data[1].split("; ")
        
        is_possible_game = True

        for draw in draws:
            if(not is_possible_game):
               break
            cubes = draw.split(", ")
            
            for cube in cubes:
                cube_data = cube.split(" ")
                if(cube_count[cube_data[1]] < int(cube_data[0])):
                    is_possible_game = False
                    break
        
        if(is_possible_game):
            total += int(game_data[0][5:])

print(total)
