def solve(input: list[str]):
    print("🎄 Solving Day 4 Part 1")
    total = 0

    for line in input:
        card_info = line[line.index(":") + 1:].split("|")
        numbers = list(map(lambda num: int(num), card_info[0].split()))
        winning_numbers = list(map(lambda num: int(num), card_info[1].split()))
        card_score = 0
        for number in numbers:
            for winning_number in winning_numbers:
                if number == winning_number:
                    if card_score == 0:
                        card_score += 1
                    else:
                        card_score *= 2
        total += card_score
        print(numbers)

    print(f"Sum of card points is: {total}")
    return total
