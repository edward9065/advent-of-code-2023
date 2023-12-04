from functools import reduce

total = 0
cube_index = {
    'red': 0,
    'green': 1,
    'blue': 2
}
with open('../input/day02.txt', encoding='utf-8') as input:
    for line in input:
        game_data = line.strip().split(": ")
        draws = game_data[1].split("; ")
        
        # not the most readable but it's [red, green, blue]
        max_count_list = [0, 0, 0]

        for draw in draws:
            cubes = draw.split(", ")
            
            for cube in cubes:
                cube_data = cube.split(" ")
                max_count_list[cube_index[cube_data[1]]] = max(max_count_list[cube_index[cube_data[1]]], int(cube_data[0]))
                
        
        power = reduce(lambda x, y: x*y, max_count_list) #better to use math.prod probably but I wanted the practice
        total += power


print(total)
