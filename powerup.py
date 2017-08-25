import random
import time
from boardobject import BoardObject


class PowerUp(BoardObject):
    # This class inherits from the BoardObject class and adds/overrides
    # methods specific to powerup like spawning it, giving the powerup and
    # whether it should be drawn or not.
    def __init__(self, row, col):
        # This method is the constructor and it calls the constructor of the
        # BoardObject class it inherits and initializes data like which powerup
        # it is, has it been used etc.
        super().__init__(row, col, 'powerup')
        self.__lastPlaced = time.clock() - 11
        self.__usedInLevel = False
        powerUps = ['XtraLife', 'HugeBomb', 'Immortal']
        self.__type = powerUps[random.randint(0, len(powerUps) - 1)]

    def addPowerUp(self):
        # This method spawns the powerup if it hasn't been used yet.
        if(self.__usedInLevel):
            return
        self.__usedInLevel = True
        self.__lastPlaced = time.clock()

    def givePowerUp(self, board):
        # This method applies the effects of the powerup.
        self.__lastPlaced = time.clock() - 11
        if(self.__type == 'XtraLife'):
            board.addLife()
        elif(self.__type == 'HugeBomb'):
            board.hugeBomb()
        elif(self.__type == 'Immortal'):
            board.makeImmortal()

    def shouldDraw(self):
        # This method returns whether the powerup has expired or not and
        # therefore, should it be drawn or not.
        return self.__lastPlaced + 10 >= time.clock()

    def getSymbols(self):
        # This method returns the symbols specific to the different type of
        # powerups.
        tempSymbols = super().getSymbols()
        for i in range(0, len(tempSymbols)):
            tempSymbols[i] = tempSymbols[i].replace('P', self.__type[i])
        return tempSymbols
