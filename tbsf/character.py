from baseconfig import *

class Character:
    def __init__(self, name, race, sex, caste):
        # Basic Attributes
        self.name = name
        self.alive = True
        self.auto_attack = False
        self.inventory = []
        # Basic Properties
        self._level = 1
        # Race
        #TODO: Allow halfbreeds
        race = race if (race in RACES) else random.choice(list(RACES))
        self._race = [race]
        self.hp_start = RACES[race][0]
        self.hp_step = RACES[race][1]
        self.hp_used = 0  # No injuries yet!
        self.mp_start = RACES[race][2]
        self.mp_step = RACES[race][3]
        self.mp_used = 0
        # Sex
        sex = sex if (sex in SEXES) else random.choice(list(SEXES))
        self.sex = sex
        self.pronouns = SEXES[sex]
        # Caste (class, profession)
        caste = caste if (caste in CASTES) else random.choice(list(CASTES))
        self._caste = [caste]
        self._casteid = [CASTES[caste][0]]
        self.hp_bonus = CASTES[caste][1]
        self.mp_bonus = CASTES[caste][2]
        # Conditions
        self.conditions = []
        # Wieldables
        self.hands_max = 2 # max number of wieldable objects
        self._hands = [None, None]
        # Armor
        #TODO: Create dictionary class for equipping armor
        # e.g. self._armor = WearableArmor()
        for a in ARMORS:
            setattr(self, a, None)

    # ARMOR
    @property
    def armor(self):
        armor_worn = []
        for a in ARMORS:
            try:
                armor_worn.append(getattr(self, a))
            except:
                pass
        return tuple(armor_worn)

    @armor.setter
    def armor(self, *args, **kwargs):
        # Use the equip() unequip() functions
        pass

    def equip(self, thing):
        try:
            assert (thing.wearable in list(ARMORS))
            assert self.isforme(thing)
            # put it on!
        except:
            # not wearable
            pass

    def unequip(self, armor):
        # check if item in _hands
        # move item to inventory
        pass

    # CASTE
    @property
    def caste(self):
        return tuple(self._caste[0:CASTE_MAX])

    @caste.setter
    def caste(self, *args, **kwargs):
        # Use the add_caste() and del_caste() functions
        pass

    @property
    def casteid(self):
        return tuple(self._casteid[0:CASTE_MAX])

    # HP
    @property
    def hp(self):
        return self.calc_p('hp')

    # LEVEL
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, new_level):
        self._level = new_level if new_level <= LEVEL_MAX else LEVEL_MAX

    def levelup(self):
        self.level = self.level + 1
        return self.level

    # MP
    @property
    def mp(self):
        return self.calc_p('mp')
    
    # RACE
    @property
    def race(self):
        return tuple(self._race)

    # EQUIPMENT - wield(), unwield()
    @property
    def wielding(self):
        return tuple(self._hands)

    def wield(self, thing):
        try:
            assert self.hands_max >= thing.wieldable >= 1
            assert self.isforme(thing)
            # if thing.wieldable > freehands: move other item to inventory
            # wield it!
        except:
            # can't wield
            pass

    def unwield(self, wieldable):
        # check if wielding
        # move item to inventory
        # set self._hands[0] to None
        pass

    # MISC
    def calc_p(self, thing):
        p_self = calc_value(self, thing)
        p_armor = calc_value(self.armor, thing)
        p_equipment = calc_value(self.wielding, thing)
        p_conditions = calc_value(self.conditions, thing)
        try:
            p_used = getattr(self, f'{thing}_used')
        except:
            p_used = 0
        
        # Sums
        p_max = p_self + p_armor + p_equipment
        p_modified = p_max + p_conditions
        p_remaining = p_max + p_conditions - p_used
        return (p_remaining, p_modified, p_max)
    
    # 
    def istype(self, me, group):
        for i in list(me):
            if (i in group):
                return True
        return False
    
    def israce(self, race_list):  # wrapper for istype()
        return self.istype(self.race, race_list)

    def iscaste(self, caste_list):  #wrapper for istype()
        return self.istype(self.caste, caste_list)

    def isforme(self, thing):
        try:
            assert self.israce(thing.race)
            assert self.iscaste(thing.caste)
            return True
        except:
            return False