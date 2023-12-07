class Race:
    time:int
    distance:int
    def __init__(self,time:int, distance:int) -> None:
        self.time = time
        self.distance = distance
        pass

    def __repr__(self) -> str:
        return f"Race: {self.time}ms, {self.distance}mm"


def solve(input: list[str]):
    print("🎄 Solving Day 6 Part 1")
    number_of_ways_total = 1
    times = input[0].split()[1:]
    distances = input[1].split()[1:]
    races: list[Race] = []
    for time_idx,time in enumerate(times):
        races.append(Race(int(time),int(distances[time_idx])))
    print(races)
    race_results = []
    for race in races:
        number_of_ways = 0
        boat_speed = 1
        for time in range(1,race.time -1):
            boat_speed = time
            travel_time = race.time - time
            traveled_distance = travel_time * boat_speed
            if traveled_distance > race.distance:
                number_of_ways += 1
        race_results.append(number_of_ways)

    print(race_results)
    for result in race_results:
        number_of_ways_total *= result
    print(f"Number of ways to beat the record is: {number_of_ways_total}")
    return number_of_ways_total
