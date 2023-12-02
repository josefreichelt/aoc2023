def solve(input: list[str]):
    print("🎄 Solving Day 2 Part 1")
    total = 0
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    for line in input:
        id = line[line.find(" "):line.find(":")]
        game_sets = line[line.find(":") + 1:].strip().split(";")

        is_invalid_game = False
        for set in game_sets:
            dice_sets = set.split(",")
            for dice in dice_sets:
                number, color = dice.strip().split(" ")
                match color:
                    case "red":
                        if int(number) > red_limit:
                            is_invalid_game = True
                    case "blue":
                        if int(number) > blue_limit:
                            is_invalid_game = True
                    case "green":
                        if int(number) > green_limit:
                            is_invalid_game = True

        if is_invalid_game:
            print(f"Invalid game {id}")
            continue
        total += int(id)
    print(f"Sum of game ids is: {total}")
    return total
