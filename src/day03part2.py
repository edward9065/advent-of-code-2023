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

def get_gear_ratio(grid: list[list[str]], row_index: int, col_index: int) -> int:
    if grid[row_index][col_index] != "*":
            return 0
    adjacent_list = []
    count = 0
    top_row = grid[row_index-1]
    mid_row = grid[row_index]
    bot_row = grid[row_index+1]

    if top_row[col_index] in digit_set:
        count += 1
        c_start = col_index
        while(c_start>0):
            c_start -= 1
            if(top_row[c_start] not in digit_set):
                c_start +=1
                break
        c_end = col_index
        while(c_end<len(top_row)):
            c_end += 1
            if(top_row[c_end] not in digit_set):
                break
        adjacent_list.append(int("".join(top_row[c_start:c_end])))

    else:
        if top_row[col_index-1] in digit_set:
            count += 1
            c_start = col_index-1
            while(c_start>0):
                c_start -= 1
                if(top_row[c_start] not in digit_set):
                    c_start +=1
                    break
            adjacent_list.append(int("".join(top_row[c_start:column_index])))
        if top_row[col_index+1] in digit_set:
            count+=1
            c_end = col_index
            while(c_end<len(top_row)):
                c_end += 1
                if(top_row[c_end] not in digit_set):
                    break
            adjacent_list.append(int("".join(top_row[column_index+1:c_end])))
    if mid_row[col_index-1] in digit_set:
        count += 1
        if count > 2:
            return 0
        c_start = col_index-1
        while(c_start>0):
            c_start -= 1
            if(mid_row[c_start] not in digit_set):
                c_start +=1
                break
        adjacent_list.append(int("".join(mid_row[c_start:column_index])))
    if mid_row[col_index+1] in digit_set:
        count+=1
        if count > 2:
            return 0
        c_end = col_index
        while(c_end<len(mid_row)):
            c_end += 1
            if(mid_row[c_end] not in digit_set):
                break
        adjacent_list.append(int("".join(mid_row[column_index+1:c_end])))
    if bot_row[col_index] in digit_set:
        count += 1
        if count > 2:
            return 0
        c_start = col_index
        while(c_start>0):
            c_start -= 1
            if(bot_row[c_start] not in digit_set):
                c_start +=1
                break
        c_end = col_index
        while(c_end<len(bot_row)):
            c_end += 1
            if(bot_row[c_end] not in digit_set):
                break
        adjacent_list.append(int("".join(bot_row[c_start:c_end])))
    else:
        if bot_row[col_index-1] in digit_set:
            count += 1
            if count > 2:
                return 0
            c_start = col_index-1
            while(c_start>0):
                c_start -= 1
                if(bot_row[c_start] not in digit_set):
                    c_start +=1
                    break
            adjacent_list.append(int("".join(bot_row[c_start:column_index])))
        if bot_row[col_index+1] in digit_set:
            count+=1
            if count > 2:
                return 0
            c_end = col_index
            while(c_end<len(bot_row)):
                c_end += 1
                if(bot_row[c_end] not in digit_set):
                    break
            adjacent_list.append(int("".join(bot_row[column_index+1:c_end])))

    if len(adjacent_list) != 2:
        return 0
    
    return adjacent_list[0]*adjacent_list[1]
    
        

                    
total = 0

with open('../input/day03.txt', encoding='utf-8') as input:
    grid = input.read().splitlines()
    grid = [list(row) for row in grid]
    grid = expand_grid(grid)

    for row_index, row in enumerate(grid[1:len(grid)]):
        column_index = 1
        while(column_index<(len(row)-1)):
            total += get_gear_ratio(grid, row_index, column_index)
            column_index += 1

print(total)