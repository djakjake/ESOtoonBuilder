#==========================#
# import external packages #
#==========================#

#=============================================================================#
# Attributes definition                                                       #
#=============================================================================#

class Attributes:

    #===========================#
    # default attribute options #
    #===========================#
    health = 0
    magicka = 0
    stamina = 0
    maxPoints = 64
    healthFactor = 122
    magickaFactor = 111
    staminaFactor = 111

    #=================================================================#
    # constructor                                                     #
    #=================================================================#

    def __init__(self, Character, **usrOp):
        # update instance options with user options
        self.__dict__.update(usrOp)
        # make sure that the sum of attribute points <= max number of
        # allowed points
        assert sum([self.health, self.magicka, self.stamina]) <= self.maxPoints, f"\n\
            \nERROR [Character.Attributes]:\
            \nThe total number of attribute points allotted to health,\
            \nmagicka, and stamina, is greater than the allowed number.\
            \nThe allowed number is set to {self.maxPoints}\
            \n(default is {Attributes.maxPoints}).\n"
        # add base stats to Character instance
        self.__AddBaseHealth(Character)
        self.__AddBaseMagicka(Character)
        self.__AddBaseStamina(Character)

    #==========================================================#
    # private functions to translate from stat points to stats #
    # NOTE: obtained from source:                              #
    #   https://elderscrollsonline.wiki.fextralife.com/Stats   #
    # which was updated on 17 Oct 2019 01:31                   #
    #==========================================================#

    def __AddBaseHealth(self, Character):
        Character.baseHealth = self.health * self.healthFactor

    def __AddBaseMagicka(self, Character):
        Character.basemagicka = self.magicka * self.magickaFactor

    def __AddBaseStamina(self, Character):
        Character.baseStamina = self.stamina * self.staminaFactor

