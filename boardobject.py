from config import Config

class BoardObject(object):
	def __init__(self, row, col, uid):
		self.__posRow = row
		self.__posCol = col
		self.__uid = uid

	def getRow(self):
		return self.__posRow

	def getCol(self):
		return self.__posCol

	def getUID(self):
		return self.__uid

	def shouldDraw(self):
		return True

	def getSymbols(self):
		return Config().getSymbols(self.__uid)

	def setPos(self, row, col):
		self.__posRow = row
		self.__posCol = col

	def areColliding(self, row, col):
		return (self.__posRow <= row+1 and row <= self.__posRow+1 and self.__posCol <= col+3 and col <= self.__posCol+3)

	def explosionHit(self, game):
		pass