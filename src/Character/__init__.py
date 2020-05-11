#==========================#
# import external packages #
#==========================#

#=============================#
# import Character submodules #
#=============================#
from . Attributes import Attributes
from . BuffFood import BuffFood
from . ChampionPoints import ChampionPoints
from . Equipment import Equipment
from . Mundus import Mundus
from . Potions import Potions
from . Race import Race
from . Skills import Skills

#============================#
# import user configurations #
#============================#
from .. config import CharacterOptions as usrOp

#=============================================================================#
# Character definition                                                        #
#=============================================================================#

class Character:


    #===========================#
    # default character options #
    #===========================#

    #==================================================================#
    # Character constructor                                            #
    #==================================================================#

    def __init__(self, *args, **kwargs):

        # add sumbodule instances
        for subModule in [
            # TODO: add PrimaryStats,
            Attributes,
            BuffFood,
            ChampionPoints,
            Equipment,
            Mundus,
            Potions,
            Race,
            Skills
        ]:
            moduleName = subModule.__module__.split('.')[-1]
            optionsDict = getattr(usrOp, moduleName)
            moduleInst = subModule(self, **optionsDict)
            setattr(self, moduleName, moduleInst)

        # TODO: update Attributes module to add stats to Character.PrimaryStats instead of Character
        # TODO: add Buffs module
        # TODO: add buffList as Buffs attribute
        # TODO: finish implementing Mundus
        # TODO: test mundus stone
        # TODO: print CharacterPrimaryStats for recurring test

