import time

from person import Person


class Bomberman(Person):
    # This class inherits from the Person class and adds/overrides methods
    # specific to bomberman like immortality powerup, getting hit by the
    # bomb/enemy.
    def __init__(self, row, col, isImmortal):
        # This method is the constructor and it calls the constructor of the
        # Person class it inherits and initializes data on whether the
        # bomberman is immortal or not.
        self.__isImmortal = isImmortal
        self.__life = 1
        # Make the bomberman immortal for the first one second, as it can't be
        # hit till time.clock() + 1 second.
        self.__lastWhenHit = time.clock()
        super().__init__(row, col, 'bomberman')

    def explosionHit(self, game):
        # This method handles what happens when the bomberman is hit by an
        # explosion or an enemy.
        if(self.__lastWhenHit + 1 < time.clock()):
            self.__lastWhenHit = time.clock()
            if(self.__isImmortal):
                pass
            else:
                self.__life -= 1
            if(self.__life <= 0):
                game.lostLife()

    def shouldDraw(self):
        # This method returns whether the enemy should be drawn or not(whether
        # it is dead or not).
        return (self.__life > 0)
