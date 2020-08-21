from Game.Shared import GameObject
from Game.Shared import GameConstants

class Enemy(GameObject):

    #constructor
    def __init__(self, position, sprite, game):
        #create and set member variables
        self.__game = game
        self.__hitPoints = 100
        self.__lives = 1
        super(Enemy, self).__init__(position, (GameConstants.ENEMY_SIZE), sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        pass

