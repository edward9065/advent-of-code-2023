#idea: find first number, then recursively find the full number + if there is a symbol next to it
digit_set = { '0','1','2','3','4','5','6','7','8','9' }
non_symbol_set = { '0','1','2','3','4','5','6','7','8','9', '.' }

def expand_grid(grid: list[list[str]]) -> list[list[str]]:
    for row in grid:
        row.insert(0, '.')
        row.append('.')      

    row_len = len(grid[0])
    grid.insert(0, ['.' for i in range(row_len)])
    grid.append(['.' for i in range(row_len)])
    return grid
    
# def get_number(row_index: int, column_index: int) -> (int, int, int, bool): 
def is_symbol_adjacent(grid: list[list[str]], row_index: int, column_index: int):
    # two for loops is arguably a worse solution than this
    return (
        grid[row_index-1][column_index-1] not in non_symbol_set or
        grid[row_index-1][column_index] not in non_symbol_set or
        grid[row_index-1][column_index+1] not in non_symbol_set or
        grid[row_index][column_index-1] not in non_symbol_set or
        grid[row_index][column_index+1] not in non_symbol_set or
        grid[row_index+1][column_index-1] not in non_symbol_set or
        grid[row_index+1][column_index] not in non_symbol_set or
        grid[row_index+1][column_index+1] not in non_symbol_set
    )
    
# returns (number, next index, is adjacent)
def get_number(grid, row_index: int, column_index: int) -> (int, int, bool): 
    row_len = len(grid[0])
    row = grid[row_index]
    number = row[column_index]
    
    symbol_adjacent = is_symbol_adjacent(grid, row_index, column_index)
    column_index +=1

    if number not in digit_set:
        return (0, column_index, symbol_adjacent)


    while(column_index<(row_len-1)):
        if row[column_index] not in digit_set:
            break
        number += row[column_index]
        symbol_adjacent = symbol_adjacent or is_symbol_adjacent(grid, row_index, column_index)
        column_index+=1


    return(int(number), column_index, symbol_adjacent)

total = 0

with open('../input/day03.txt', encoding='utf-8') as input:
    grid = input.read().splitlines()
    grid = [list(row) for row in grid]
    grid = expand_grid(grid)
    # print(grid)
    for row_index, row in enumerate(grid[1:len(grid)]):
        column_index = 1
        while(column_index<(len(row)-1)):
            number, column_index, symbol_adjacent = get_number(grid, row_index, column_index)
            if symbol_adjacent:
                total += number
            
print(total)