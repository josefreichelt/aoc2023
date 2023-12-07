cardValues = {
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


class Hand:
    rank: int
    bid: int

    def __init__(self, rank: int, bid: int) -> None:
        self.time = rank
        self.bid = bid
        pass

    def __repr__(self) -> str:
        return f"Hand: {self.time}ms, {self.distance}mm"


def solve(input: list[str]):
    print("🎄 Solving Day 7 Part 1")
    number_of_winnings = 1
    
    print(f"Total winning are: {number_of_winnings}")
    return number_of_winnings
