import time
import random

from person import Person


class Enemy(Person):
    # This class inherits from the Person class and adds/overrides methods
    # specific to enemies like their special symbols, their movement logic.
    def __init__(self, row, col, enemyInfo):
        # This method is the constructor and it calls the constructor of the
        # Person class it inherits and loads data from config and initializes
        # the information.
        super().__init__(row, col, 'enemy')
        self.__lastMoved = time.clock()
        self.__speed = enemyInfo['moveInterval']
        self.__lastDirection = 1
        self.__life = enemyInfo['numberOfBombs']
        self.__lastWhenHit = time.clock()
        self.__enemySymbols = enemyInfo['symbols']

    def shouldDraw(self):
        # This method returns whether the enemy should be drawn or not(whether
        # it is dead or not).
        return (self.__life > 0)

    def explosionHit(self, game):
        # This method handles what happens when the enemy is hit by a bomb.
        if(self.__lastWhenHit + 1 < time.clock()):
            self.__lastWhenHit = time.clock()
            if(self.__life > 0 and self.__life - 1 <= 0):
                game.addToScore(100)
            self.__life -= 1

    def move(self, direction):
        # This method checks whether the enemy can move or not according to the
        # last moved time and if it can, the inherited move method is called.
        if(time.clock() < self.__lastMoved + self.__speed):
            return
        super().move(direction)
        self.__lastMoved = time.clock()
        self.__lastDirection = direction

    def enemyMove(self, boardObjects):
        # This method moves the enemies in a pseudo-random manner.
        canMoveArray = [False] * 5
        canMoveCount = 0
        directions = [1, 2, 3, 4]
        random.shuffle(directions)
        didItMove = False

        # Calculate for each of the direction whether the enemy can move there
        # or not.
        for direction in directions:
            if(self.canMove(direction, boardObjects)):
                canMoveArray[direction] = True
                canMoveCount += 1

        # If the enemy can keep moving in the same direction, either keep
        # moving in that directon or switch direction to its left or right. If
        # the enemy can't move in the last direction, either turn back or
        # randomly switch to any direction which it can move in.
        if(canMoveArray[self.__lastDirection]):
            if(random.randint(1, 4) != 1 or canMoveCount == 1):
                self.move(self.__lastDirection)
            else:
                for direction in directions:
                    if(canMoveArray[direction] and (direction % 2 != self.__lastDirection % 2)):
                        self.move(direction)
                        didItMove = True
                        break
                if(not didItMove):
                    self.move(self.__lastDirection)
        else:
            if(canMoveArray[1 + ((self.__lastDirection - 1) ^ 2)] and random.randint(1, 4) != 1):
                self.move(1 + ((self.__lastDirection - 1) ^ 2))
            else:
                for direction in directions:
                    if(canMoveArray[direction]):
                        self.move(direction)
                        break

    def getSymbols(self):
        # This method returns the symbols for each different kind of enemy.
        tempSymbols = super().getSymbols()
        for i in range(0, len(tempSymbols)):
            tempSymbols[i] = tempSymbols[i].replace(
                'E', self.__enemySymbols[i])
        return tempSymbols
