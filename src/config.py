# configuration/options

#=============================================================================#
# Character Options                                                           #
#=============================================================================#

class CharacterOptions:

    #========================================================================#
    # attribute points                                                       #
    # NOTE: defaults values can be found in                                  #
    # src/Character/Attributes/__init__.py under "default attribute options" #
    #========================================================================#

    Attributes = {
        # number of attribute points in:
        'health': 64,
        'magicka': 0,
        'stamina': 0,
        # the maximum number of allowed attribute points
        'maxPoints': 64,
        # scale factor used to calculate base stats from attribute points:
        'healthFactor': 122,
        'magickaFactor': 111,
        'staminaFactor': 111,
    }

    #=================#
    # buff food/drink #
    #=================#

    BuffFood = {
    }

    #=================#
    # champion points #
    #=================#

    ChampionPoints = {
    }

    #===========#
    # equipment #
    #===========#

    Equipment = {
    }

    #========#
    # mundus #
    #========#

    Mundus = {
    }

    #=========#
    # potions #
    #=========#

    Potions = {
    }

    #======#
    # race #
    #======#

    Race = {
    }

    #========#
    # skills #
    #========#

    Skills = {
    }

#=============================================================================#
# Design of Experiment Options                                                #
#=============================================================================#

class DOE:
    pass

#=============================================================================#
# Simulation Options                                                          #
#=============================================================================#

class Sim:
    pass

#=============================================================================#
# Optimization Options                                                        #
#=============================================================================#

class Optimization:
    pass

