def solve(input: list[str]):
    print("🎄 Solving Day 2 Part 2")
    total = 0
    for line in input:
        game_sets = line[line.find(":") + 1:].strip().split(";")

        min_red_cubes = 0
        min_green_cubes = 0
        min_blue_cubes = 0

        for set in game_sets:
            dice_sets = set.split(",")
            for dice in dice_sets:
                number, color = dice.strip().split(" ")
                match color:
                    case "red":
                        min_red_cubes = max(min_red_cubes, int(number))
                    case "blue":
                        min_blue_cubes = max(min_blue_cubes, int(number))
                    case "green":
                        min_green_cubes = max(min_green_cubes, int(number))
        power = min_red_cubes * min_blue_cubes * min_green_cubes
        print(f"Power of a game {power}")
        total += int(power)
    print(f"Sum of game powers is: {total}")
    return total
