from baseconfig import ARMORS, CASTES, CONDITIONS, DAMAGES, LEVEL_MAX, RACES, RANGE_DEFAULT
from baseconfig import sanitize
from conditions import CONDITIONS

class GameItem:
    def __init__(self, name, *, add_condition=None, del_condition=None,
            caste=list(CASTES), race=list(RACES), level=0, 
            armor_bonus=0, armor_group=None, armor_range=RANGE_DEFAULT,
            damage_bonus=0, damage_group=None, damage_range=RANGE_DEFAULT,
            hp_bonus=0, mp_bonus=0, wearable=None):

        self.name = name
        self.wearable = sanitize(wearable, ARMORS)
        self.wieldable = 1  # player.hands >= item.wieldable >= 0: wieldable

        self.add_condition = sanitize(add_condition, CONDITIONS)
        self.del_condition = sanitize(del_condition, CONDITIONS)
        self.caste = sanitize(caste, CASTES)
        self.damage_bonus = damage_bonus
        self.damage_group = sanitize(damage_group, DAMAGES)
        self.damage_range = damage_range
        self.hp_bonus = hp_bonus
        self.level = level if level <= LEVEL_MAX else LEVEL_MAX
        self.mp_bonus = mp_bonus
        self.armor_bonus = armor_bonus
        self.armor_group = sanitize(armor_group, DAMAGES)
        self.armor_range = armor_range
        self.race = sanitize(race, RACES)

class Headgear(GameItem):
    def __init__(self, name, **kwargs):
        GameItem.__init__(self, name, **kwargs)
        self.wearable = sanitize('armor_head', ARMORS)

class BodyArmor(GameItem):
    def __init__(self, name, **kwargs):
        GameItem.__init__(self, name, **kwargs)
        self.wearable = sanitize('armor_body', ARMORS)
        self.wieldable = 2

class HandArmor(GameItem):
    def __init__(self, name, **kwargs):
        GameItem.__init__(self, name, **kwargs)
        self.wearable = sanitize('armor_hands', ARMORS)

class LegArmor(GameItem):
    def __init__(self, name, **kwargs):
        GameItem.__init__(self, name, **kwargs)
        self.wearable = sanitize('armor_legs', ARMORS)

class Footwear(GameItem):
    def __init__(self, name, **kwargs):
        GameItem.__init__(self, name, **kwargs)
        self.wearable = sanitize('armor_feet', ARMORS)
