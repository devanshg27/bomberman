from boardobject import BoardObject

class Bricks(BoardObject):
	def __init__(self, row, col):
		super().__init__(row, col, 'bricks')
