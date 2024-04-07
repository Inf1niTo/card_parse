from dataclasses import dataclass


@dataclass
class Food:
    id: int
    title: str
    link: str
    address: str
    location: str
    priceRange: str
    time: str
    number: str
