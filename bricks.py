from boardobject import BoardObject

class Bricks(BoardObject):
	def __init__(self, row, col):
		super().__init__(row, col, 'bricks')
		self.__alive = 1

	def explosionHit(self, game):
		self.__alive = 0

	def shouldDraw(self):
		return (self.__alive > 0)
