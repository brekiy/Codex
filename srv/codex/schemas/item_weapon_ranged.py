from attack import Attack
from trait import Trait

class ItemWeaponRanged():
    def __init__(self, name: str, weight: float, range_inc: int, shoot: Attack, melee: Attack, crit_mult: int, traits: list[Trait], mgt_requirement: int, price: int):
        self.name = name
        self.weight = weight
        self.range_inc = range_inc
        self.shoot = shoot
        self.melee = melee
        self.crit_mult = crit_mult
        self.traits = traits
        self.mgt_requirement = mgt_requirement
        self.price = price
