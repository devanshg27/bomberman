from boardobject import BoardObject

class Explosion(BoardObject):
	def __init__(self, row, col):
		super().__init__(row, col, 'explosion')