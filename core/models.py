from dataclasses import dataclass

@dataclass
class Crop:
    name: str
    yield_per_acre: float
    price_per_kg: float
    costs: dict