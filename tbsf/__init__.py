"""Turn-Based Strategy Framework in Python3"""

# This module is a shameless rip-off of the original Guild Wars game. It
# is not endorsed by, affiliated with, maintained, authorized, nor
# sponsored by ArenaNet, NCsoft, Guild Wars, etc, or its affiliates.

__version__ = "0.1.001"
__license__ = "MIT"

from .character import Character
from .condition import Condition
from .equipment import Equipment

# Basic Armor
from .equipment import Headgear, BodyArmor, HandArmor, LegArmor, Footwear
