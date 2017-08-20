from enemy import Enemy
from explosion import Explosion
from config import Config
from bomberman import Bomberman
from bomb import Bomb
from wall import Wall
from bricks import Bricks

import random
import time

class Board(object):
	def __init__(self, game, level):
		self.__text = ['abc'] * 40
		self.__game = game
		self.__boardObjects = []
		self.__noOfRows = Config().getBoardSize('rows')
		self.__noOfCols = Config().getBoardSize('cols')
		self.__explosions = []
		self.__lastExplosionTime = time.clock()
		self.__bombRange = 1

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
		self.__levelInfo = Config().getLevel(level)
		freeBlocks = random.sample(freeBlocks, len(self.__levelInfo['enemies']) + self.__levelInfo['noOfBricks'])
		
		for row, col in freeBlocks[0 : self.__levelInfo['noOfBricks']]:
			self.__boardObjects.append(Bricks(row, col))
		
		for i in range(0, len(self.__levelInfo['enemies'])):
			row, col = freeBlocks[self.__levelInfo['noOfBricks'] + i]
			self.__boardObjects.append(Enemy(row, col, self.__levelInfo['enemies'][i]))

		self.__bombermanIndex = len(self.__boardObjects)
		self.__boardObjects.append(Bomberman(2, 4))

	def __addToBoard(self, boardState, row, col, symbols):
		boardState[row][col : col + 4] = symbols[0 : 4]
		boardState[row + 1][col : col + 4] = symbols[4 : 8]
		return boardState

	def getCurrentState(self):
		boardState = [[' '] * (self.__noOfCols + 5) for i in range(0, self.__noOfRows)]
		for boardObject in self.__boardObjects:
			if(boardObject.shouldDraw()):
				self.__addToBoard(boardState, boardObject.getRow(), boardObject.getCol(), boardObject.getSymbols())
		for explosion in self.__explosions:
			self.__addToBoard(boardState, explosion.getRow(), explosion.getCol(), explosion.getSymbols())
		return list(map(lambda x: ''.join(x), boardState))

	def move(self, direction):
		if(self.__boardObjects[self.__bombermanIndex].canMove(direction, self.__boardObjects)):
			self.__boardObjects[self.__bombermanIndex].move(direction)

	def dropBomb(self):
		if(self.__boardObjects[-1].getUID() == 'bomb'):
			return
		else:
			bombermanObject = self.__boardObjects[self.__bombermanIndex]
			self.__boardObjects.append(Bomb(2*(bombermanObject.getRow()//2), 4*((bombermanObject.getCol()+1)//4)))

	def updateState(self):
		for boardObject in self.__boardObjects:
			if(boardObject.shouldDraw() and boardObject.getUID() == 'enemy'):
				boardObject.enemyMove(self.__boardObjects)
			elif(boardObject.getUID() == 'bomb' and boardObject.hasExploded()):
				self.addExposion(boardObject.getRow(), boardObject.getCol())
				del self.__boardObjects[-1]

		if(len(self.__explosions) > 0 and self.__lastExplosionTime + 0.5 < time.clock()):
			self.__explosions[:] = []

	def addExposion(self, row, col):
		diff = [[-1, 0], [0, 1], [1, 0], [0, -1]]
		self.__lastExplosionTime = time.clock()
		for direction in diff:
			for len in range(0, 1+self.__bombRange):
				foundWall = False
				foundBricks = False
				curRow = row + (len*2*direction[0])
				curCol = col + (len*4*direction[1])
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
		bombermanObject = self.__boardObjects[self.__bombermanIndex]
		for boardObject in self.__boardObjects:
			if(boardObject.shouldDraw() and boardObject.getUID() == 'enemy' and boardObject.areColliding(bombermanObject.getRow(), bombermanObject.getCol())):
				bombermanObject.explosionHit(self.__game)

		for explosion in self.__explosions:
			for boardObject in self.__boardObjects:
				if(boardObject.areColliding(explosion.getRow(), explosion.getCol())):
					boardObject.explosionHit(self.__game)

