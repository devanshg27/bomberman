import time
from boardobject import BoardObject

class Bomb(BoardObject):
	def __init__(self, row, col):
		super().__init__(row, col, 'bomb')
		self.__bombTime = time.clock()

	def getSymbols(self):
		return list(map(lambda x: x.replace('O', str(int(self.__bombTime + 4 - time.clock()))), super().getSymbols()))

	def hasExploded(self):
		return self.__bombTime + 3 <= time.clock()