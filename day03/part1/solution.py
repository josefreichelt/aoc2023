def is_symbol(char: str):
    return not char.isdigit() and char != "."


def solve(input: list[str]):
    print("🎄 Solving Day 3 Part 1")
    total = 0

    for line_idx, line in enumerate(input):
        is_valid_part = False
        part_numbers = []
        current_part = []
        for digit_idx, digit in enumerate(line):
            if digit.isdigit():
                current_part.append(digit)

                if line_idx != 0:
                    # Check Top Left
                    if digit_idx > 0 and not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx - 1][digit_idx - 1])
                    # Check Top
                    if not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx - 1][digit_idx])
                    # Check Top Right
                    if digit_idx + 1 < len(input[line_idx - 1]) and not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx - 1][digit_idx + 1])

                # Check Left
                if digit_idx > 0 and not is_valid_part:
                    is_valid_part = is_symbol(line[digit_idx - 1])
                # Check Right
                if digit_idx + 1 < len(line) and not is_valid_part:
                    is_valid_part = is_symbol(line[digit_idx + 1])

                if line_idx + 1 < len(input):
                    # Check Bottom Left
                    if digit_idx > 0 and not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx + 1][digit_idx - 1])
                    # Check Bottom
                    if not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx + 1][digit_idx])
                    # Check Bottom Right
                    if digit_idx + 1 < len(input[line_idx + 1]) and not is_valid_part:
                        is_valid_part = is_symbol(input[line_idx + 1][digit_idx + 1])

            if (not digit.isdigit() and len(current_part) > 0) or digit_idx + 1 == len(line):
                if is_valid_part:
                    part_numbers.append("".join(current_part))
                    is_valid_part = False
                current_part = []

        # print(part_numbers)
        for part in part_numbers:
            total += int(part)

    print(f"Sum of part numbers is: {total}")
    return total
