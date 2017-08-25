from boardobject import BoardObject


class Explosion(BoardObject):
    # This class inherits from the BoardObject class and passes the uid
    # specific to the Explosion object.
    def __init__(self, row, col):
        # This method is the constructor and it calls the constructor of the
        # BoardObject class it inherits.
        super().__init__(row, col, 'explosion')
