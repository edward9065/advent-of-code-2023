from operator import itemgetter
import sys
class interval_list: 

    def __init__(self, category: list[list[int]] = [[]]):
        self.starts = []
        self.ends = []
        self.destinations = []

        category.sort(key=itemgetter(1))
        for item in category:
            self.starts.append(item[1])
            self.ends.append(item[1] + item[2] - 1)
            self.destinations.append(item[0])

    def __repr__(self):
        return f'{self.starts}, {self.ends}, {self.destinations}'        
    
    def get_destination(self, source: int):
        for i in range(len(self.starts)):
            if source >= self.starts[i] and source <= self.ends[i]:
                return self.destinations[i] + source - self.starts[i]  

        return source

    def get_destination_from_interval(self, start: int, length: int):
        min_val = sys.maxsize
        min_non_overlapped_value_found = False
        end = start+length-1
        last_end = end

        for i in range(len(self.starts)):
            if not((start > self.ends[i]) or (end < self.starts[i])):

                if(start > self.starts[i]):

                    min_val = min(min_val, self.get_destination(start))
                    if not min_non_overlapped_value_found:
                        if self.starts[i] > (last_end + 1):
                            min_val = min(min_val, last_end+1)
                            min_non_overlapped_value_found = True
                        last_end = self.ends[i]
                else: 
                    if i == 0:
                        min_val = min(start, self.get_destination(self.starts[i]))
                        min_non_overlapped_value_found = True
                    else:
                        min_val = min(min_val, self.get_destination(self.starts[i]))
            else: 
                break
        return min_val


with open('../input/day05.txt', encoding='utf-8') as input:
    data = input.read().split("\n\n")
    # print(data)
seeds = data[0]
seeds = seeds.split(": ")[1].split(" ")

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
    category_maps[index_to_category_list[i]] = interval_list(data[i+1])
    

def get_location(seed: int, len) -> int: 
    soil = category_maps["seed_to_soil"].get_destination_from_interval(seed, len)
    fertilizer = category_maps["soil_to_fertilizer"].get_destination(soil)
    water = category_maps["fertilizer_to_water"].get_destination(fertilizer)
    light = category_maps["water_to_light"].get_destination(water)
    temperature = category_maps["light_to_temperature"].get_destination(light)
    humidity = category_maps["temperature_to_humidity"].get_destination(temperature)
    return category_maps["humidity_to_location"].get_destination(humidity)

closest_location = get_location(int(seeds[0]), int(seeds[1]))

for i in range(2, len(seeds), 2):
    closest_location = min(closest_location, min(closest_location, get_location(int(seeds[i]), int(seeds[i+1]))))
    

print(closest_location)
    