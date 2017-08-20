import time
import random

from person import Person

class Enemy(Person):
	def __init__(self, row, col):
		super().__init__(row, col, 'enemy')
		self.__lastMoved = time.clock()
		self.__speed = 0.12
		
		self.__lastDirection = 1

	def move(self, direction):
		if(time.clock() < self.__lastMoved + self.__speed):
			return
		super().move(direction)
		self.__lastMoved = time.clock()
		self.__lastDirection = direction

	def enemyMove(self, boardObjects):
		canMoveArray = [False] * 5
		canMoveCount = 0
		directions = [1, 2, 3, 4]
		random.shuffle(directions)
		
		for direction in directions:
			if(self.canMove(direction, boardObjects)):
				canMoveArray[direction] = True
				canMoveCount += 1

		if(canMoveArray[self.__lastDirection]):
			if(random.randint(1, 4) != 1 or canMoveCount == 1):
				self.move(self.__lastDirection)
			else:
				for direction in directions:
					if(canMoveArray[direction] and (direction % 2 != self.__lastDirection % 2) ):
						self.move(direction)
						break
		else:
			if(canMoveArray[1 + ((self.__lastDirection - 1) ^ 2)] and random.randint(1, 4) != 1):
				self.move(1 + ((self.__lastDirection - 1) ^ 2))
			else:
				for direction in directions:
					if(canMoveArray[direction]):
						self.move(direction)
						break
