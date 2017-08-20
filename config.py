class Config(object):
	def __init__(self):
		self.__symbols = {
			'wall' : ['\033[0;33mX', 'X', 'X', 'X\033[0m', '\033[0;33mX', 'X', 'X', 'X\033[0m'],
			'bricks' : ['\033[1;33m/', '/', '/', '/\033[0m', '\033[1;33m/', '/', '/', '/\033[0m'],
			'bomberman' : ['\033[0;36m[', '^', '^', ']\033[0m', '\033[0;36m ', ']', '[', ' \033[0m'],
			'enemy' : ['\033[0;31mE', '\033[0;31mE', '\033[0;31mE', '\033[0;31mE\033[0m', '\033[0;31mE', '\033[0;31mE', '\033[0;31mE', '\033[0;31mE\033[0m'],
			'explosion' : ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
			'bomb' : ['\033[0;35mO\033[0m'] * 8, 
		}
		self.__levels = {
			1 : {
				'enemies' : [0.12, 0.2, 0.1, 0.12, 0.12, 0.2],
				'noOfBricks' : 50,
			}
		}
		self.__boardSize = {
			'rows' : 42,
			'cols' : 84,
		}
	def getSymbols(self, key):
		return self.__symbols[key]

	def getBoardSize(self, key):
		return self.__boardSize[key]

	def getLevel(self, key):
		return self.__levels[key]