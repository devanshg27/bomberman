from boardobject import BoardObject


class Bricks(BoardObject):
    # This class inherits from the BoardObject class and adds/overrides
    # methods specific to bricks like it shouldn't be drawn after destruction,
    # and adds scores fo destruction.
    def __init__(self, row, col):
        # This method is the constructor and it calls the constructor of the
        # BoardObject class it inherits and initializes data on whether the
        # bricks are destroyed or not.
        super().__init__(row, col, 'bricks')
        self.__alive = 1

    def explosionHit(self, game):
        # This method handles what happens when the bricks are hit by an
        # explosion.
        if(self.__alive):
            game.addToScore(20)
        self.__alive = 0

    def shouldDraw(self):
        # This method returns True if the bricks should be drawn(if they
        # haven't been destroyed).
        return (self.__alive > 0)
