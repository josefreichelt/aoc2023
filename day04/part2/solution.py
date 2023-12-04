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
    for card in cards:
        print(f"Processing: {card.card_id}")
        next_cards_to_copy = 0
        for number in card.numbers:
            for winning_number in card.winning_numbers:
                if number == winning_number:
                    next_cards_to_copy += 1
        print(f"Coppying next {next_cards_to_copy} cards")
        cards_to_process = filter(lambda c: int(c.card_id) in range(
            int(card.card_id) + 1, int(card.card_id) + next_cards_to_copy + 1), cards.copy())
        print("Cards to process")
        print(list(cards_to_process))
        
        # for coppied_cards in range(next_cards_to_copy):
        amount += process_card_list(list(cards_to_process))

    return amount


def solve(input: list[str]):
    print("🎄 Solving Day 4 Part 2")
    cards: list[Card] = []
    for line in input:
        card_id = line[line.index(" ") + 1:line.index(":")].strip()
        print(card_id)
        card_info = line[line.index(":") + 1:].split("|")
        numbers = list(map(lambda num: int(num), card_info[0].split()))
        winning_numbers = list(map(lambda num: int(num), card_info[1].split()))
        cards.append(Card(card_id, numbers, winning_numbers))
    total = process_card_list(cards)

    print(f"Total number of scratchcards is: {total}")
    return total
