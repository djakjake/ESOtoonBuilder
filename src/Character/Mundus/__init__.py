#==========================#
# import external packages #
#==========================#
import sys

#=============================================================================#
# Mundus definition                                                           #
#=============================================================================#

class Mundus:

    # the stone provided through the user options must be in the following list
    allowedList = [
        None,
        'Lady',
        'Lover',
        'Lord',
        'Mage',
        'Tower',
        'Atronach',
        'Serpent',
        'Shadow',
        'Ritual',
        'Thief',
        'Warrior',
        'Apprentice',
        'Steed',
    ]
    # the default Mundus stone
    stone = None

    #=================================================================#
    # constructor                                                     #
    #=================================================================#

    def __init__(self, Character, **usrOp):
        # add user options as Mundus instance attributes
        self.__dict__.update(usrOp)
        # add the stone to character using public function
        self.AddStone(Character, self.stone)

    #==================================================================#
    # AddStone                                                         #
    #==================================================================#

    def AddStone(self, Character, stone):
        """
        Input:
        Character (Character Instance)
        stone (string)

        Description:
        Checks that the provided stone is allowed and adds the stone,
        and any effects, to the Character instance
        """
        # make sure that Mundus instance stone is allowed
        if stone not in Mundus.allowedList:
            printAllowed = [(f'\n    {x}') for x in Mundus.allowedList]
            sys.exit(f"\n\
                \nError [Character.Mundus]:\
                \nThe Mundus stone provided ({self.stone}),\
                \nis not in the allowed list.\
                \nPlease use one of the following: {printAllowed}"
            )
        # add the stone to the Character->Buffs->buffList
        stoneName = f"The {self.stone}"
        if stoneName not in Character.Buffs.buffList:
            Character.Buffs.buffList.append(stoneName)
            # construct the function call from the stone name
            funcCall = f"self.__AddStone_{stone}(Character)"
            # execute the function call
            exec(funcCall)

    #==================================================================#
    # __AddStone_<stone>                                               #
    # source:                                                          #
    # https://elderscrollsonline.wiki.fextralife.com/Mundus+Stones     #
    # source updated:                                                  #
    # 02 Dec 2019 02:03                                                #
    #==================================================================#

    def __AddStone_None(Character):
        pass

    def __AddStone_Lady(Character):
        Character.PrimaryStats.physicalResistance += 2752
        Character.PrimaryStats.spellResistance += 2752

    def __AddStone_Lover(Character):
        Character.PrimaryStats.physicalPenetration += 2752
        Character.PrimaryStats.spellPenetration += 2752
        pass

    def __AddStone_Lord(Character):
        pass

    def __AddStone_Mage(Character):
        pass

    def __AddStone_Tower(Character):
        pass

    def __AddStone_Atronach(Character):
        pass

    def __AddStone_Serpent(Character):
        pass

    def __AddStone_Shadow(Character):
        pass

    def __AddStone_Ritual(Character):
        pass

    def __AddStone_Thief(Character):
        pass

    def __AddStone_Warrior(Character):
        pass

    def __AddStone_Apprentice(Character):
        pass

    def __AddStone_Steed(Character):
        pass
