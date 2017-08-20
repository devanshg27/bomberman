import os
import sys
import termios
import atexit
from select import select

class KeyBoard:
	def __init__(self):
		# Save the terminal settings
		self.fd = sys.stdin.fileno()
		self.new_term = termios.tcgetattr(self.fd)
		self.old_term = termios.tcgetattr(self.fd)

		# New terminal setting unbuffered
		self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
		termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

		# Support normal-terminal reset at exit
		atexit.register(self.set_normal_term)
		
	def set_normal_term(self):
		termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

	def getch(self):
		# Returns a keyboard character after kbhit() has been called.
		ch = sys.stdin.read(1)
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)
		return ch		

	def kbhit(self):
		# Returns True if keyboard character was hit, False otherwise.
		dr, dw, de = select([sys.stdin], [], [], 0)
		return dr != []


class GameInput(object):
	def __init__(self, game):
		self.__game = game
		self.__kb = KeyBoard()

	def checkInput(self, game):
		if(self.__kb.kbhit()):
			ch = self.__kb.getch()
			if(ch == 'q'): self.__game.endGame()
			elif(ch == 'w'): self.__game.move(1)
			elif(ch == 'd'): self.__game.move(2)
			elif(ch == 's'): self.__game.move(3)
			elif(ch == 'a'): self.__game.move(4)
			elif(ch == 'b'): self.__game.dropBomb()
			elif(ch == 'p'): self.__game.powerUp()