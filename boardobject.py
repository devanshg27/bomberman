from config import Config


class BoardObject(object):
    # This class stores data common for all the board objects like the row
    # number, column number of their top left corner and methods like
    # getSymbols or are colliding.
    def __init__(self, row, col, uid):
        # This method is the constructor and it initializes data like which
        # rowand column should the object be placed and its uid.
        self.__posRow = row
        self.__posCol = col
        self.__uid = uid

    def getRow(self):
        # This method returns the row the object is on.
        return self.__posRow

    def getCol(self):
        # This method returns the column the object is on.
        return self.__posCol

    def getUID(self):
        # This method returns the UID(Unique IDentifier) for the specific type
        # of object.
        return self.__uid

    def shouldDraw(self):
        # This method returns whether the object should be drawn or not(by
        # default they are alwasy drawn).
        return True

    def getSymbols(self):
        # This method returns the symbols specific to the UID after loading
        # them from the config.
        return Config().getSymbols(self.__uid)

    def setPos(self, row, col):
        # This method sets the position of the board Object.
        self.__posRow = row
        self.__posCol = col

    def areColliding(self, row, col):
        # This method checks whether an object whose top left corner is on
        # (row, col) would collide with this board object.
        return (
            self.__posRow <= row +
            1 and row <= self.__posRow +
            1 and self.__posCol <= col +
            3 and col <= self.__posCol +
            3)

    def explosionHit(self, game):
        # This method stores what happens when this object is hit by an
        # explosion(by default, nothing happens).
        pass
