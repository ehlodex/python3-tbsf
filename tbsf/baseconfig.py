import random
from conditions import Condition

RANGE_DEFAULT = (1, 2)
INVENTORY_MAX = 32  # maximum number of carryable items
LEVEL_MAX = 20  # maximum attainable level by self.levelup()
DAMAGE_MIN = 1  # minimum damaged caused by combat
DAMAGES = ['cold', 'earth', 'fire', 'lightning', 'blunt', 'piercing', 'slashing', 'chaos', 'holy', 'dark', 'shadow']
CASTE_MAX = 2   # maximum number of applicable castes

ARMORS = ('armor_head', 'armor_body', 'armor_hands', 'armor_legs', 'armor_feet')

CONDITIONS = {}

RACES = { # race_name: (hp_start, hp_step, mp_start, mp_step)
    'dwarf': (120, 25, 20, 0),
    'elf': (120, 15, 20, 0),
    'hobbit': (130, 20, 20, 0),
    'human': (100, 20, 20, 0),
    'orc': (120, 20, 20, 0)
}

SEXES = { # gender_name: (pronouns)
    'male': ('he', 'him', 'his', 'his', 'himself'),
    'female': ('she', 'her', 'her', 'hers', 'herself'),
    'asexual': ('it', 'it', 'its', 'its', 'itself')
}

CASTES = { # caste_name: (class_id, hp_bonus, mp_bonus)
    'elemental': ('El', 0, 10),
    'mesmer': ('Me', 0, 10),
    'monk': ('Mo', 0, 10),
    'necromancer': ('Ne', 0, 10),
    'ranger': ('Ra', 0, 5),
    'warrior': ('Wa', 20, 0)
}


def get_random(r_min=RANGE_DEFAULT, r_max=None):
    r_min = listify(r_min)
    r_max = listify(r_max)
    t_range = listify(r_min + r_max)
    t_range = t_range if t_range else RANGE_DEFAULT
    r_min = t_range[0]
    r_max = t_range[-1]
    del t_range
    return random.randint(r_min, r_max)


def intlist(thing):
    listed = []
    if isinstance(thing, tuple) or isinstance(thing, list):
        for i in thing:
            if i not in listed:
                try:
                    i = int(float(i))
                    listed.append(i)
                except:
                    pass
        return sorted(listed)
    else:
        return [thing]


def sanitize(thing, group):
    if isinstance(thing, str) or not thing:
        thing = [thing]
    else:
        thing = list(thing)
    
    for t in thing:
        if (t not in group):
            thing.remove(t)
    return thing


def calc_value(group, thing):
    total = 0
    if not isinstance(group, list) and not isinstance(group, tuple):
        group = [group]
    for i in group:
        # check for start, step, level
        try:
            thing_start = getattr(i, f'{thing}_start')
            thing_step = getattr(i, f'{thing}_step')
            thing_level = (i.level - 1) if i.level > 0 else 0
        except:
            thing_start = thing_step = thing_level = 0
        # check for bonus
        try:
            total += getattr(i, f'{thing}_bonus')
        except:
            pass
        total += thing_start + (thing_step * thing_level)
    return total