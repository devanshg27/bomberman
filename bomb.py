import time
from boardobject import BoardObject


class Bomb(BoardObject):
    # This class inherits from the BoardObject class and adds/overrides
    # methods specific to the bomb class like displaying the number of seconds
    # left and whether the bomb has exploded.
    def __init__(self, row, col):
        # This method is the constructor and it calls the constructor of the
        # BoardObject class it inherits and initializes data on when the bomb
        # was placed.
        super().__init__(row, col, 'bomb')
        self.__bombTime = time.clock()

    def getSymbols(self):
        # This method returns the data to be displayed which is the number of
        # seconds left.
        timeLeft = str(int(self.__bombTime + 4 - time.clock()))
        return list(map(lambda x: x.replace('O',
                                            timeLeft),
                        super().getSymbols()))

    def hasExploded(self):
        # This method returns whether the bomb has exploded.
        return self.__bombTime + 3 <= time.clock()
