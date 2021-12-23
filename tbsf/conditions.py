import random

# Conditions are very basic for now. They have a fixed bonus that is
# independent of the characters race and caste, being determined solely
# by their percent_chance of being applied.

class Condition:
    def __init__(self, name, percent_chance=100, description='', *,
            armor_bonus=0, damage_bonus=0, hp_bonus=0, mp_bonus=0):
        self.name = name
        self.description = description
        self._armor = armor_bonus
        self._damage = damage_bonus
        self._hp = hp_bonus
        self._mp = mp_bonus
        self.odds = float(percent_chance/100)

    @property
    def armor_bonus(self):
        return self.calc_bonus(self._armor)

    @property
    def damage_bonus(self):
        return self.calc_bonus(self._damage)

    @property
    def hp_bonus(self):
        return self.calc_bonus(self._hp)

    @property
    def mp_bonus(self):
        return self.calc_bonus(self._mp)

    def calc_bonus(self, bonus):
        if self.odds >= random.random():
            return bonus
        else:
            return 0

CONDITIONS = {
    'blessed': Condition('Blessed', 100, 'Increases max hp and mp', hp_bonus=20, mp_bonus=10),
    'blindness': Condition('Blindness', 50, 'Causes player to miss target (50% chance)', damage_bonus=-999),
    'cursed': Condition('Cursed', 100, 'Decreases max hp and mp', hp_bonus=-10, mp_bonus=-5)
}
