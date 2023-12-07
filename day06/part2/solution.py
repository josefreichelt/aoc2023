class Race:
    time: int
    distance: int

    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance
        pass

    def __repr__(self) -> str:
        return f"Race: {self.time}ms, {self.distance}mm"


def solve(input: list[str]):
    print("🎄 Solving Day 6 Part 2")
    number_of_ways_total = 0
    times = ''.join(input[0].split()[1:])
    distances = ''.join(input[1].split()[1:])
    print(times)
    print(distances)
    race = Race(int(times), int(distances))
    boat_speed = 1
    for time in range(1, race.time - 1):
        boat_speed = time
        travel_time = race.time - time
        traveled_distance = travel_time * boat_speed
        if traveled_distance > race.distance:
            number_of_ways_total += 1

    print(f"Number of ways to beat the record is: {number_of_ways_total}")
    return number_of_ways_total
