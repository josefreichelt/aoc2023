def is_symbol(char: str):
    return not char.isdigit() and char != "."


class Part:
    x = 0
    y = 0
    val = ""

    def __init__(self, x, y, val) -> None:
        self.x = x
        self.y = y
        self.val = val

    def __repr__(self) -> str:
        return f"Part x:{self.x},y:{self.y}\nval:{self.val}"

    def is_overlaping(self, x: int, y: int):
        length = len(self.val) - 1
        return x >= self.x and x <= self.x + length and y == self.y


class Gear:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.parts: list[Part] = []

    def __repr__(self) -> str:
        return f"\nGear: x:{self.x},y:{self.y}\n{self.parts}\n\n"


def solve(input: list[str]):
    print("🎄 Solving Day 3 Part 2")
    total = 0
    gears: list[Gear] = []
    max_y_pos = len(input) - 1
    max_x_pos = len(input[0])
    parts: list[Part] = []
    # Parse the grid
    for line_idx, line in enumerate(input):
        part = []
        for digit_idx, digit in enumerate(line):
            if digit == "*":
                gears.append(Gear(digit_idx, line_idx))
            if digit.isdigit():
                part.append(digit)
            # Part number ended
            if (not digit.isdigit() and len(part) > 0) or digit_idx == max_x_pos:
                parts.append(Part(digit_idx - len(part), line_idx, line[digit_idx - len(part):digit_idx]))
                part = []

    for gear in gears:
        # Previous row
        if gear.y != 0:
            possible_parts = filter(lambda part: part.y == gear.y - 1, parts)
            for part in possible_parts:
                if part.is_overlaping(gear.x - 1, gear.y - 1) or part.is_overlaping(gear.x, gear.y - 1) or part.is_overlaping(gear.x + 1, gear.y - 1):
                    gear.parts.append(part)
        possible_parts = filter(lambda part: part.y == gear.y, parts)
        for part in possible_parts:
            if part.is_overlaping(gear.x - 1, gear.y) or part.is_overlaping(gear.x + 1, gear.y):
                gear.parts.append(part)
        possible_parts = filter(lambda part: part.y == gear.y + 1, parts)
        for part in possible_parts:
            if part.is_overlaping(gear.x - 1, gear.y + 1) or part.is_overlaping(gear.x, gear.y + 1) or part.is_overlaping(gear.x + 1, gear.y + 1):
                gear.parts.append(part)
    gears = list(filter(lambda gear: len(gear.parts) == 2, gears))
    for gear in gears:
        total += int(gear.parts[0].val) * int(gear.parts[1].val)

    print(f"Sum of gear ratios is: {total}")
    return total
