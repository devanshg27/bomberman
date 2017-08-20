import time

from display import Display
from gameinput import GameInput
from board import Board

class Game(object):
	def __init__(self):
		self.__level = 1
		self.__display = Display(self)
		self.__board = Board(self, 1)
		self.__gameInput = GameInput(self)

	def startGame(self):
		# self.__player = Player(self.__level, 3, 3)
		self.isGameRunning = True
		while self.isGameRunning:
			# self.__win.handle_events(self.__player)
			self.__display.render(self.__board.getCurrentState())
			self.__board.checkStatus()
			self.__gameInput.checkInput(self)
			self.__board.updateState()
			# time.sleep(0.12)
			# self.__player.update()
			# for entity in self.__level.copy():
			# 	entity.update()

	def endGame(self):
		self.isGameRunning = False
		self.__display.close()

	def move(self, direction):
		# direction : 1 for up, 2 for right, 3 for down and 4 for left
		self.__board.move(direction)

	def dropBomb(self):
		self.__board.dropBomb()

	def powerUp(self):
		pass

if __name__ == '__main__':
	game = Game()
	game.startGame()