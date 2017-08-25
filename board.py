from enemy import Enemy
from explosion import Explosion
from config import Config
from bomberman import Bomberman
from bomb import Bomb
from door import Door
from wall import Wall
from bricks import Bricks
from powerup import PowerUp

import random
import time


class Board(object):
        # This class implements methods for the control of the flow of each
        # level and stores relevant data.
    def __init__(self, game, level, livesLeft):
        # This method is the constructor and it initializes data for this
        # level.
        self.__game = game
        self.__livesLeft = livesLeft
        self.__boardObjects = []
        self.__noOfRows = Config().getBoardSize('rows')
        self.__noOfCols = Config().getBoardSize('cols')
        self.__explosions = []
        self.__lastExplosionTime = time.clock()
        self.__bombRange = 1
        self.__startTime = time.clock()
        self.__levelNumber = level

        # Store the freebolcks in a list while adding the walls.
        freeBlocks = []
        for row in range(0, self.__noOfRows, 2):
            for col in range(0, self.__noOfCols, 4):
                if(row == 0 or col == 0 or row + 2 == self.__noOfRows or col + 4 == self.__noOfCols):
                    self.__boardObjects.append(Wall(row, col))
                elif(row % 4 == 0 and col % 8 == 0):
                    self.__boardObjects.append(Wall(row, col))
                else:
                    freeBlocks.append([row, col])
        freeBlocks.remove([2, 4])
        freeBlocks.remove([2, 8])
        freeBlocks.remove([4, 4])

        # Get information about the level.
        self.__levelInfo = Config().getLevel(level)

        # Choose random block from the freeBlocks array.
        freeBlocks = random.sample(freeBlocks, len(
            self.__levelInfo['enemies']) + self.__levelInfo['noOfBricks'] + 1)

        # Choose random bricks behind which the door will be placed
        doorPosition = random.randint(0, self.__levelInfo['noOfBricks'] - 1)

        # Add the door and the brciks.
        for row, col in freeBlocks[0: self.__levelInfo['noOfBricks']]:
            if([row, col] == freeBlocks[doorPosition]):
                self.__doorIndex = len(self.__boardObjects)
                self.__boardObjects.append(Door(row, col))
            self.__boardObjects.append(Bricks(row, col))

        row, col = freeBlocks[self.__levelInfo['noOfBricks']]

        # Add the powerup.
        self.__powerUpIndex = len(self.__boardObjects)
        self.__boardObjects.append(PowerUp(row, col))

        # Add the enemies.
        for i in range(0, len(self.__levelInfo['enemies'])):
            row, col = freeBlocks[self.__levelInfo['noOfBricks'] + i + 1]
            self.__boardObjects.append(
                Enemy(row, col, self.__levelInfo['enemies'][i]))

        # Add the bomberman.
        self.__bombermanIndex = len(self.__boardObjects)
        self.__boardObjects.append(Bomberman(2, 4, False))

    def __addToBoard(self, boardState, row, col, symbols):
        # This method adds the object to the current board state string.
        boardState[row][col: col + 4] = symbols[0: 4]
        boardState[row + 1][col: col + 4] = symbols[4: 8]
        return boardState

    def getCurrentState(self):
        # This method returns the current state as an array of strings.
        boardState = [[' '] * (self.__noOfCols + 5)
                      for i in range(0, (self.__noOfRows + 3))]
        for boardObject in self.__boardObjects:
            if(boardObject.shouldDraw()):
                self.__addToBoard(
                    boardState,
                    boardObject.getRow(),
                    boardObject.getCol(),
                    boardObject.getSymbols())
        for explosion in self.__explosions:
            self.__addToBoard(
                boardState,
                explosion.getRow(),
                explosion.getCol(),
                explosion.getSymbols())
        # add the information about the current game.
        boardState[-2] = '\tTime Left: ' + format(int(self.__startTime + self.__levelInfo['levelTime'] + 1 - time.clock(
        )), '3d') + '\t\tLives: ' + str(self.__livesLeft) + '\tScore: ' + str(self.__game.getScore())
        boardState[-1] = '\t\t\t\tStage: ' + \
            format(int(self.__levelNumber), '1d')
        return list(map(lambda x: ''.join(x), boardState))

    def move(self, direction):
        # This method moves the bomberman.
        if(self.__boardObjects[self.__bombermanIndex].canMove(direction, self.__boardObjects)):
            self.__boardObjects[self.__bombermanIndex].move(direction)

    def addPowerUp(self):
        # This method adds the powerup at a random position.
        self.__boardObjects[self.__powerUpIndex].addPowerUp()

    def dropBomb(self):
        # This method drops the bomb at current position of bomberman.
        if(self.__boardObjects[-1].getUID() == 'bomb'):
            return
        else:
            bombermanObject = self.__boardObjects[self.__bombermanIndex]
            self.__boardObjects.append(Bomb(
                2 * (bombermanObject.getRow() // 2), 4 * ((bombermanObject.getCol() + 1) // 4)))

    def updateState(self):
        # This method moves the enemies and shows the explosion from the bomb
        # and removes the explosions when time has passed.
        for boardObject in self.__boardObjects:
            if(boardObject.shouldDraw() and boardObject.getUID() == 'enemy'):
                boardObject.enemyMove(self.__boardObjects)
            elif(boardObject.getUID() == 'bomb' and boardObject.hasExploded()):
                self.addExposion(boardObject.getRow(), boardObject.getCol())
                del self.__boardObjects[-1]

        if(len(self.__explosions) > 0 and self.__lastExplosionTime + 0.5 < time.clock()):
            self.__explosions[:] = []

    def addExposion(self, row, col):
        # This method adds the explosions around the bomb.
        diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.__lastExplosionTime = time.clock()
        self.__explosions.append(Explosion(row, col))
        for direction in diff:
            for len in range(1, 1 + self.__bombRange):
                foundWall = False
                foundBricks = False
                curRow = row + (len * 2 * direction[0])
                curCol = col + (len * 4 * direction[1])
                for boardObject in self.__boardObjects:
                    if(boardObject.getUID() == 'wall' and curRow == boardObject.getRow() and curCol == boardObject.getCol()):
                        foundWall = True
                    elif(boardObject.getUID() == 'bricks' and boardObject.shouldDraw() and curRow == boardObject.getRow() and curCol == boardObject.getCol()):
                        foundBricks = True
                if(foundWall):
                    break
                self.__explosions.append(Explosion(curRow, curCol))
                if(foundBricks):
                    break

    def checkStatus(self):
        # This method if any enemy or explosion is colliding with bomberman or
        # any enemy collides with an explosion and takes necessary action.
        bombermanObject = self.__boardObjects[self.__bombermanIndex]
        for boardObject in self.__boardObjects:
            if(boardObject.shouldDraw() and boardObject.getUID() == 'enemy' and boardObject.areColliding(bombermanObject.getRow(), bombermanObject.getCol())):
                bombermanObject.explosionHit(self.__game)

        for explosion in self.__explosions:
            for boardObject in self.__boardObjects:
                if(boardObject.areColliding(explosion.getRow(), explosion.getCol())):
                    boardObject.explosionHit(self.__game)

        doorObject = self.__boardObjects[self.__doorIndex]
        if(doorObject.getRow() == bombermanObject.getRow() and doorObject.getCol() == bombermanObject.getCol()):
            enemyCount = 0
            for boardObject in self.__boardObjects:
                if(boardObject.shouldDraw() and boardObject.getUID() == 'enemy'):
                    enemyCount += 1
            if(enemyCount == 0):
                self.__game.nextLevel()

        powerUpObject = self.__boardObjects[self.__powerUpIndex]
        if(powerUpObject.shouldDraw() and powerUpObject.getRow() == bombermanObject.getRow() and powerUpObject.getCol() == bombermanObject.getCol()):
            powerUpObject.givePowerUp(self)

        if(self.__startTime + self.__levelInfo['levelTime'] < time.clock()):
            self.__game.lostLife()

    def addLife(self):
        # This methods adds a life(when we get a powerup).
        self.__livesLeft += 1
        self.__game.addLife()

    def hugeBomb(self):
        # This methods makes the bomb huge(when we get a powerup).
        self.__bombRange += 1

    def makeImmortal(self):
        # This methods makes the bomberman immortal(when we get a powerup).
        bombermanObject = self.__boardObjects[self.__bombermanIndex]
        self.__boardObjects[self.__bombermanIndex] = Bomberman(
            bombermanObject.getRow(), bombermanObject.getCol(), True)
