def word_to_number(word: str) -> int:
    match word:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return -1


def solve(input: list[str]):
    print("🎄 Solving Day 1 Part 2")

    valid_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for line in input:
        first_found_num_index = -1
        last_found_num_index = -1
        last_text_digit_index = -1
        first_text_digit_idx = -1

        # Search for text numbers
        for num_idx, num in enumerate(valid_numbers):
            first_idx = line.find(num)
            last_idx = line.rfind(num)

            if first_idx >= 0 and first_found_num_index == -1:
                first_found_num_index = first_idx
                first_text_digit_idx = num_idx
            elif first_idx <= first_found_num_index and first_idx >= 0:
                first_found_num_index = first_idx
                first_text_digit_idx = num_idx
            if last_idx >= 0 and last_found_num_index == -1:
                last_found_num_index = last_idx
                last_text_digit_index = num_idx
            elif last_idx >= last_found_num_index and last_idx >= 0:
                last_found_num_index = last_idx
                last_text_digit_index = num_idx

        first_number = 0
        last_number = 0

        # Convert found text digit index into actual int
        if first_text_digit_idx >= 0:
            first_number = word_to_number(valid_numbers[first_text_digit_idx])
        if last_text_digit_index >= 0:
            last_number = word_to_number(valid_numbers[last_text_digit_index])

        # Search for regular digit number
        for char_idx, char in enumerate(line):
            if char.isdigit():
                if char_idx <= first_found_num_index and first_found_num_index != -1:
                    first_found_num_index = char_idx
                    first_number = int(char)
                elif first_found_num_index == -1:
                    first_found_num_index = char_idx
                    first_number = int(char)
                if char_idx >= last_found_num_index and last_found_num_index != -1:
                    last_found_num_index = char_idx
                    last_number = int(char)
                elif last_found_num_index == -1:
                    last_found_num_index = char_idx
                    last_number = int(char)

        total += int(f"{first_number}{last_number}")

    print(f"Trebuchet calibration value is: {total}")
    return total
