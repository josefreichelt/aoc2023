def solve(input: list[str]):
    print("🎄 Solving Day 1 Part 1")
    total = 0
    for line in input:
        digits = list(filter(str.isdigit, line))
        pair = list(digits[i] for i in [0, -1])
        total += int(pair[0] + pair[1])

    print(f"Trebuchet calibration value is: {total}")
    return total
