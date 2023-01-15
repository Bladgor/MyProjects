
from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


card = Card("Q", "hearts")

print(card)
print(card)
