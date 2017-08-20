from boardobject import BoardObject

class Wall(BoardObject):
	def __init__(self, row, col):
		super().__init__(row, col, 'wall')