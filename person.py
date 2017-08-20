from boardobject import BoardObject

class Person(BoardObject):
	def __init__(self, row, col, uid):
		super().__init__(row, col, uid)
	
	def move(self, direction):
		diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
		super().setPos(super().getRow() + diff[direction-1][0], super().getCol() + diff[direction-1][1])

	def canMove(self, direction, boardObjects):
		diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
		tempRow = super().getRow() + diff[direction-1][0]
		tempCol = super().getCol() + diff[direction-1][1]
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