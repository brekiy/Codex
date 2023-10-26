from attack import Attack
from trait import Trait

class MeleeWeapon():
    def __init__(self, name: str, weight: float, swing: Attack, thrust: Attack, crit_mult: int, traits: list[Trait], mgt_requirement: int, price: int):
        self.name = name
        self.weight = weight
        self.swing = swing
        self.thrust = thrust
        self.crit_mult = crit_mult
        self.traits = traits
        self.mgt_requirement = mgt_requirement
        self.price = price
