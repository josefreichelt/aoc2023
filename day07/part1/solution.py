CARD_VALUES = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

from functools import cmp_to_key


class Hand:
    rank: int
    bid: int
    rank_decider: int
    total_cards_value: int
    cards: dict[str, int]
    raw_cards: str

    def __init__(self, cards: str, bid: int) -> None:
        self.rank = 0
        self.bid = int(bid)
        self.rank_decider = 0
        self.cards = {}
        card_types = {}
        self.total_cards_value = 0
        self.raw_cards = cards
        for card in cards:
            card_types.setdefault(card, 0)
            card_types[card] += 1
        sort = sorted(card_types.items(), key=lambda card: card[1], reverse=True)
        for (sorted_cards_key, sorted_card_value) in sort:
            self.cards[sorted_cards_key] = sorted_card_value
        # for idx, key in enumerate(sorted_cards_keys):
        #     self.cards[key] = sorted_card_values[idx]
        pass

    def __repr__(self) -> str:
        return f"rank{self.rank}|total:{self.total_cards_value}|{self.raw_cards}|{self.bid}"
        # return f"\nHand: rank{self.rank}-{self.rank_decider} 🃏 {self.total_cards_value} \nbid {self.bid}\n{self.cards}"


def hand_compare(hand1: Hand, hand2: Hand):
    for idx in range(len(hand1.raw_cards)):
        card1_value = CARD_VALUES[hand1.raw_cards[idx]]
        card2_value = CARD_VALUES[hand2.raw_cards[idx]]
        # print(
        #     f"Comparing {hand1.raw_cards}|{hand1.raw_cards[idx]} {card1_value} and {hand2.raw_cards}|{hand2.raw_cards[idx]} {card2_value}")
        if card1_value < card2_value:
            return -1
        elif card1_value > card2_value:
            return 1
        else:
            continue
    return 0


def solve(input: list[str]):
    print("🎄 Solving Day 7 Part 1")
    number_of_winnings = 0 
    hands: list[Hand] = []
    # Parse
    for line in input:
        [cards, bid] = line.split()
        hands.append(Hand(cards, bid))

    # Calculate hands
    for hand in hands:
        is_five_of_kind = False
        is_four_of_kind = False
        is_full_house = False
        is_three_of_kind = False
        is_two_pair = False
        is_one_pair = False
        is_high_card = False

        for card, count in hand.cards.items():
            # Five of a kind
            match count:
                case 5:
                    hand.rank = 7
                    is_five_of_kind = True
                    hand.total_cards_value = 5 * CARD_VALUES[card]
                case 4:
                    hand.rank = 6
                    is_four_of_kind = True
                    hand.total_cards_value = 4 * CARD_VALUES[card]
                case 3:
                    is_three_of_kind = True
                    hand.total_cards_value = 3 * CARD_VALUES[card]
                case 2:
                    if is_three_of_kind:
                        is_full_house = True
                        is_three_of_kind = False
                        hand.rank = 5
                        hand.total_cards_value += 2 * CARD_VALUES[card]
                        break
                    if is_one_pair:
                        is_one_pair = False
                        is_two_pair = True
                        hand.rank = 3
                        continue
                    if not is_one_pair:
                        is_one_pair = True
                        hand.rank = 2
                    hand.total_cards_value += 2 * CARD_VALUES[card]
                case 1:
                    hand.total_cards_value += CARD_VALUES[card]
                    if is_four_of_kind:
                        hand.rank_decider = CARD_VALUES[card]
                    elif is_three_of_kind:
                        hand.rank = 4
                    elif not is_full_house and not is_one_pair and not is_two_pair and not is_high_card:
                        hand.rank = 1
                        is_high_card = True

        # print(hand)
        # if is_five_of_kind:
        #     print(f"Five of kind")
        # elif is_four_of_kind:
        #     print(f"Four of kind")
        # elif is_full_house:
        #     print(f"Full house")
        # elif is_three_of_kind:
        #     print(f"Three of kind")
        # elif is_two_pair:
        #     print(f"Two pairs")
        # elif is_one_pair:
        #     print(f"One Pair")
        # elif is_high_card:
        #     print(f"High Card")
        # else:
        #     print("Dunno")
        # print("")

    # Sort hands
    hands_map: dict[int, list[Hand]] = {}
    current_rank_level = 1
    for hand in hands:
        hands_map.setdefault(hand.rank, [])
        hands_map[hand.rank].append(hand)
    sort = sorted(hands_map.items(), key=lambda hand: hand[0])
    # print(sort)
    for (sorted_hands_base_rank, sorted_hands) in sort:
        # print(sorted_hands_base_rank)
        sorted_by_value = sorted(sorted_hands, key=cmp_to_key(hand_compare),reverse=False)
        for hand in sorted_by_value:
            hand.rank = current_rank_level
            number_of_winnings += hand.rank * hand.bid
            current_rank_level += 1
            # print(hand)

    print(f"Total winning are: {number_of_winnings}")
    return number_of_winnings
