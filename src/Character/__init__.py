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
    # constructor                                                      #
    #==================================================================#

    def __init__(self, *args, **kwargs):

        # add sumbodule instances
        for subModule in [
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

        # TODO: test-delete
        for attr in ['health', 'stamina', 'magica']:
            attrValue = getattr(self.Attributes, attr)
            print(f"{attr} = {attrValue}")
