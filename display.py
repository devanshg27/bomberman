class Display(object):
	def __init__(self, game):
		print("\033[?1049h\033[H")
		print("\033[?25l")
		self.__game = game

	def render(self, board):
		print("\033[1;1H", end='')
		for i in range(0, len(board)):
			print(board[i])

	def close(self):
		print ("\033[?25h\033[?1049l", end='')
