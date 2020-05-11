# configuration/options

#=============================================================================#
# Character Options                                                           #
#=============================================================================#

class CharacterOptions:

    # TODO: add PrimaryStats

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
        # Pick the Mundus Stone (use quote). Available Options:
        #   None, (no quotes)
        #   'Lady',
        #   'Lover',
        #   'Lord',
        #   'Mage',
        #   'Tower',
        #   'Atronach',
        #   'Serpent',
        #   'Shadow',
        #   'Ritual',
        #   'Thief',
        #   'Warrior',
        #   'Apprentice',
        #   'Steed',
        'stone': 'Lady',
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

class DOEoptions:
    pass

#=============================================================================#
# Simulation Options                                                          #
#=============================================================================#

class SimOptions:
    pass

#=============================================================================#
# Optimization Options                                                        #
#=============================================================================#

class OptimizationOptions:
    pass

