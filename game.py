import time
import signal

from display import Display
from gameinput import GameInput
from board import Board
from config import Config


class Game(object):
    # This class implements methods for the control of the flow of the game
    # and stores relevant data.
    def __init__(self):
        # This method is the constructor and initializes data like current
        # level, score etc.
        self.__level = 1
        self.__display = Display(self)
        self.__lives = 3
        self.__board = Board(self, self.__level, self.__lives)
        self.__gameInput = GameInput(self)
        self.__score = 0
        self.__isGameRunning = True

    def startGame(self):
        # This method starts the game and continues calling relevant functions
        # till it doesn't end.
        while self.__isGameRunning:
            self.__display.render(self.__board.getCurrentState())
            self.__board.checkStatus()
            self.__gameInput.checkInput(self)
            self.__board.updateState()

    def addToScore(self, scoreToAdd):
        # This method adds scoreToAdd to score.
        self.__score += scoreToAdd

    def getScore(self):
        # This method returns the current score.
        return self.__score

    def endGame(self, infoText):
        # This method ends the game.
        self.__isGameRunning = False
        self.__display.close(infoText)

    def lostLife(self):
        # This method handles what happens when we lose a life.
        self.__lives -= 1
        if(self.__lives > 0):
            self.__board = Board(self, self.__level, self.__lives)
        else:
            self.endGame('You lost the game. Your score was ' +
                         str(self.getScore()))

    def nextLevel(self):
        # This method advances the game to the next level.
        self.__level += 1
        if(Config().isLevel(self.__level)):
            self.__board = Board(self, self.__level, self.__lives)
        else:
            self.endGame('You won the game. Your score was ' +
                         str(self.getScore()))

    def move(self, direction):
        # This method moves the bomberman in direction specified.
        # direction : 1 for up, 2 for right, 3 for down and 4 for left
        self.__board.move(direction)

    def dropBomb(self):
        # This method drops the bomb at the position bomberman is on.
        self.__board.dropBomb()

    def powerUp(self):
        # This method spawns a powerup at any position on the board.
        self.__board.addPowerUp()

    def addLife(self):
        # This method adds a life to the game.
        self.__lives += 1


if __name__ == '__main__':
    # If the game.py was started.

    # Initialize the game Object.
    game = Game()

    # This code handles what happens when Ctrl-C is pressed.
    def signal_handler(signal, frame):
        game.endGame('You quit the game')

    signal.signal(signal.SIGINT, signal_handler)

    # Start the game.
    game.startGame()
