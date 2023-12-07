class Seed:
    value: int
    mapped_values: dict[str, list[int]]

    def __init__(self, val: str) -> None:
        self.value = val
        self.mapped_values = {}
        self.mapped_values["seed"] = [int(val)]

    def __repr__(self) -> str:
        return f"🌱:{self.mapped_values}"


class SeedMap:
    dest_ranges: list[int]
    source_ranges: list[int]
    range_sizes: list[int]

    from_type: str
    to_type: str

    def __init__(self, from_type: str, to_type: str) -> None:
        self.dest_ranges = []
        self.source_ranges = []
        self.range_sizes = []
        self.from_type = from_type
        self.to_type = to_type

    def __repr__(self) -> str:
        return f"\n🗺️:{self.from_type}->{self.to_type}\n{self.source_ranges}"


def solve(input: list[str]):
    print("🎄 Solving Day 5 Part 2")
    lowest_location = 0
    seeds: list[Seed] = []
    maps: list[SeedMap] = []
    current_map = None
    # Parse stuff
    for line_idx, line in enumerate(input):
        if line.startswith("seeds:"):
            vals = line[line.index(":") + 1:].split()
            for value_index in range(0,len(vals),2):
                range_start = int(vals[value_index])
                range_length = int(vals[value_index+1])
                for ranged_seed_value in range(range_start,range_start+range_length):
                    seeds.append(Seed(ranged_seed_value))
            # print("Created seeds")

        if line[0].isdigit() and current_map != None:
            # print("Adding to existing map")
            dest, source, size = line.split()
            current_map.dest_ranges.append(int(dest))
            current_map.source_ranges.append(int(source))
            current_map.range_sizes.append(int(size))
        if line.find("map:") != -1:
            if current_map != None:
                # print("Closing map")
                maps.append(current_map)
                current_map = None
            type = line.split("-")
            current_map = SeedMap(type[0], type[2].split()[0])
            # print("Creating map")
        if line_idx + 1 == len(input):
            maps.append(current_map)
            current_map = None
    current_map = None
    for _ in (maps):
        # Find output map
        for map_inner in maps:
            if current_map == None:
                if map_inner.from_type == "seed":
                    current_map = map_inner
                    break
            else:
                if map_inner.from_type == current_map.to_type:
                    current_map = map_inner
                    break

        for seed in seeds:
            seed_value = seed.mapped_values[current_map.from_type][0]
            seed.mapped_values[current_map.to_type] = []
            is_seed_mapped = False
            for map_range_idx in range(len(current_map.dest_ranges)):
                current_dest = current_map.dest_ranges[map_range_idx]
                current_source = current_map.source_ranges[map_range_idx]
                current_range = current_map.range_sizes[map_range_idx]

                is_seed_mapped = seed_value >= current_source and seed_value < current_source + current_range
                if is_seed_mapped:
                    offset = current_source - current_dest
                    mapped_value = seed_value - offset
                    seed.mapped_values[current_map.to_type].append(mapped_value)
                    break
            if not is_seed_mapped and seed_value not in seed.mapped_values[current_map.to_type]:
                seed.mapped_values[current_map.to_type].append(seed_value)

            if current_map.to_type == "location":
                if lowest_location == 0:
                    lowest_location = seed.mapped_values["location"][0]
                lowest_location = min(seed.mapped_values["location"][0], lowest_location)

    print(f"Lowest seed location is: {lowest_location}")
    return lowest_location
