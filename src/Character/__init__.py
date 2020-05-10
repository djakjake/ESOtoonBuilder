#==========================#
# import external packages #
#==========================#

#=============================#
# import Character submodules #
#=============================#
from . Attributes import Attributes as Attr
from . BuffFood import BuffFood as BF
from . ChampionPoints import ChampionPoints as CP
from . Equipment import Equipment as Equip
from . Mundus import Mundus
from . Potions import Potions as Pots
from . Race import Race

#============================#
# import user configurations #
#============================#
from .. import config


#=============================================================================#
# Character definition                                                        #
#=============================================================================#

class Character:

    #==================================================================#
    # constructor                                                      #
    #==================================================================#

    def __init__(self, *args, **kwargs):
        pass
