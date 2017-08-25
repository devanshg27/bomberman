class Config(object):
    # This class stores all the config related to the game like the size of
    # the board, the symbols for each of the board objects and the information
    # about the enemies like speed, number of bombs required and also data
    # about each level like list of enemies, time of level and number of
    # bricks.
    def __init__(self):
        # This method is the constructor and it initializes all the
        # configuration for the game in their respective placs.
        self.__symbols = {
            'wall': ['\033[0;33mX\033[0m'] * 8,
            'bricks': ['\033[1;33m/\033[0m'] * 8,
            'bomberman': list(map(lambda x: '\033[0;36m' + x + '\033[0m',
                                  '[^^] ][ ')),
            'enemy': ['\033[0;31mE\033[0m'] * 8,
            'explosion': ['\033[1;37me\033[0m'] * 8,
            'bomb': ['\033[0;35mO\033[0m'] * 8,
            'door': ['\033[1;32mD\033[0m'] * 8,
            'powerup': ['\033[0;34mP\033[0m'] * 8,
        }
        self.__enemy1 = {
            'moveInterval': 0.22,
            'numberOfBombs': 1,
            'symbols': 'EEEEEEEE'
        }
        self.__enemy2 = {
            'moveInterval': 0.17,
            'numberOfBombs': 1,
            'symbols': '/==\\\\==/'
        }
        self.__enemy3 = {
            'moveInterval': 0.12,
            'numberOfBombs': 2,
            'symbols': '(--)===='
        }
        self.__levels = {1: {'enemies': [self.__enemy1] * 5,
                             'noOfBricks': 30,
                             'levelTime': 160,
                             },
                         2: {'enemies': [self.__enemy1,
                                         self.__enemy1,
                                         self.__enemy1,
                                         self.__enemy2,
                                         self.__enemy2,
                                         self.__enemy3],
                             'noOfBricks': 40,
                             'levelTime': 170,
                             },
                         3: {'enemies': [self.__enemy2,
                                         self.__enemy2,
                                         self.__enemy2,
                                         self.__enemy3,
                                         self.__enemy3,
                                         self.__enemy3,
                                         self.__enemy3],
                             'noOfBricks': 50,
                             'levelTime': 200,
                             },
                         }
        self.__boardSize = {
            'rows': 42,
            'cols': 84,
        }

    def getSymbols(self, key):
        # This method returns the symbol for the board object given.
        return self.__symbols[key]

    def isLevel(self, key):
        # This method returns true if the level exists in the game, else False.
        return (key in self.__levels)

    def getBoardSize(self, key):
        # This method returns the board size.
        return self.__boardSize[key]

    def getLevel(self, key):
        # This method returns the information related to the given level.
        return self.__levels[key]
