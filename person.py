from boardobject import BoardObject


class Person(BoardObject):
    # This class inherits from the BoardObject class and adds methods specific
    # to persons(enemies and bomberman).
    def __init__(self, row, col, uid):
        # This method is the constructor and it calls the constructor of the
        # BoardObject class it inherits.
        super().__init__(row, col, uid)

    def move(self, direction):
        # This method moves the person in the direction specified one block at
        # a time.
        diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        super().setPos(super().getRow() +
                       diff[direction - 1][0], super().getCol() + diff[direction - 1][1])

    def canMove(self, direction, boardObjects):
        # This method checks that can the person in the direction specified.
        diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # tempRow and tempCol store the location of the person temporarily.
        tempRow = super().getRow() + diff[direction - 1][0]
        tempCol = super().getCol() + diff[direction - 1][1]
        # Check each wall, brick or bomb on the board and check if the person
        # can collide with this object after the move.
        for boardObject in boardObjects:
            if(boardObject.getUID() == 'wall'):
                if(boardObject.areColliding(tempRow, tempCol)):
                    return False
            elif(boardObject.getUID() == 'bricks' and boardObject.shouldDraw()):
                if(boardObject.areColliding(tempRow, tempCol)):
                    return False
            elif(boardObject.getUID() == 'bomb' and not boardObject.areColliding(super().getRow(), super().getCol())):
                if(boardObject.areColliding(tempRow, tempCol)):
                    return False
        return True
