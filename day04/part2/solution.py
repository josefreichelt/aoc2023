class Card:
    card_id = ""
    numbers: list[int]
    winning_numbers = list[int]

    def __init__(self, id: str, numbers: list[int], win_numbers: list[int]) -> None:
        self.card_id = id
        self.numbers = numbers
        self.winning_numbers = win_numbers

    def __repr__(self) -> str:
        return f"🃏: {self.card_id}"


def process_card_list(cards: list[Card]):
    amount = 0
    card_multiplier: dict[str, int] = {}
    for card in cards:
        current_multiplier = card_multiplier.get(card.card_id, 1)
        # print(f"Multiplier {current_multiplier} - {range(current_multiplier)}")
        for _ in range(current_multiplier):
            # print(f"Processing: {card.card_id}")
            next_cards_to_copy = int(card.card_id)
            amount += 1
            for number in card.numbers:
                for winning_number in card.winning_numbers:
                    if number == winning_number:
                        next_cards_to_copy += 1
                        # print(f"Winning card")
                        if str(next_cards_to_copy) not in card_multiplier:
                            card_multiplier[str(next_cards_to_copy)] = 1
                        card_multiplier[str(next_cards_to_copy)] += 1
    return amount


def solve(input: list[str]):
    print("🎄 Solving Day 4 Part 2")
    cards: list[Card] = []
    for line in input:
        card_id = line[line.index(" ") + 1:line.index(":")].strip()
        card_info = line[line.index(":") + 1:].split("|")
        numbers = list(map(lambda num: int(num), card_info[0].split()))
        winning_numbers = list(map(lambda num: int(num), card_info[1].split()))
        cards.append(Card(card_id, numbers, winning_numbers))
    total = process_card_list(cards)

    print(f"Total number of scratchcards is: {total}")
    return total
