from person import Person

class Bomberman(Person):
	def __init__(self, row, col):
		self.__life = 1
		super().__init__(row, col, 'bomberman')

	def explosionHit(self, game):
		self.__life -= 1
		game.endGame()

	def shouldDraw(self):
		return (self.__life > 0)