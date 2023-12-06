from operator import itemgetter

# assumes map interval list is sorted
def get_destination_intervals(source_interval_list, map_interval_list):
    destination_interval_list = []
    for source in source_interval_list:
        temp = []
        for map in map_interval_list:
            if source[0] <= map[1] and source[1] >= map[0]:
                interval = (max(source[0], map[0]), min(source[1], map[1]))
                temp.append(interval)
                shift = map[0] - map[2]
                interval = (interval[0] - shift, interval[1] - shift)
                destination_interval_list.append(interval)
        if len(temp) > 0:
            if(source[0] < temp[0][0]): 
                destination_interval_list.append((source[0], temp[0][0]-1))
            if(source[1] > temp[-1][1]):
                destination_interval_list.append((temp[-1][1]+1, source[1]))
        elif len(temp) == 0: 
            destination_interval_list.append(source)
        for i in range(len(temp)-1):
            if(temp[i][1] < temp[i+1][0] - 1):
                destination_interval_list.append((temp[i][1], temp[i+1][0]))
    return destination_interval_list

with open('../input/day05.txt', encoding='utf-8') as input:
    data = input.read().split("\n\n")
    # print(data)
seeds = data[0].split(": ")[1].split(" ")
seed_intervals = []
for i in range(0, len(seeds), 2):
    seed_intervals.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1])-1))

index_to_category_list = [
    "seed_to_soil",
    "soil_to_fertilizer",
    "fertilizer_to_water",
    "water_to_light",
    "light_to_temperature",
    "temperature_to_humidity",
    "humidity_to_location",
]

category_maps = {
    "seed_to_soil": None,
    "soil_to_fertilizer": None,
    "fertilizer_to_water": None,
    "water_to_light": None,
    "light_to_temperature": None,
    "temperature_to_humidity": None,
    "humidity_to_location": None,
}

for i, listing in enumerate(data[1:]):
    data[i+1] = listing.split("\n")[1:]
    for j, category in enumerate(data[i+1]):
        data[i+1][j] = [int(num) for num in category.split(" ")]
    data[i+1].sort(key=itemgetter(1))
    category_maps[index_to_category_list[i]] = [(b, b+c-1, a) for [a,b,c] in data[i+1]]

soils = get_destination_intervals(seed_intervals, category_maps["seed_to_soil"])
fertilizers = get_destination_intervals(soils, category_maps["soil_to_fertilizer"])
water = get_destination_intervals(fertilizers, category_maps["fertilizer_to_water"])
light = get_destination_intervals(water, category_maps["water_to_light"])
temperatures = get_destination_intervals(light, category_maps["light_to_temperature"])
humidities = get_destination_intervals(temperatures, category_maps["temperature_to_humidity"])
locations = get_destination_intervals(humidities, category_maps["humidity_to_location"])

min_location = locations[0][0]
for i in range(1, len(locations)):
    min_location = min(locations[i][0], min_location)

# print(sorted(locations, key=itemgetter(0)))
print(min_location)
