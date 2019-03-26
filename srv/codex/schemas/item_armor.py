from trait import Trait

class ItemArmor():
    def __init__(self, name: str, weight: float, resistances: list[str], vulnerabilities: list[str], damage_reduction: dict, traits: list[Trait], mgt_requirement: int, price: int):
        self.name = name
        self.weight = weight
        self.resistances = resistances
        self.vulnerabilities = vulnerabilities
        self.damage_reduction = damage_reduction
        self.traits = traits
        self.mgt_requirement = mgt_requirement
        self.price = price
