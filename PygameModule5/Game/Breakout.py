import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout:

    #CTOR
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0, 0), 0)
        self.__balls = [
            Ball((0, 0), 0, self)
            ]



    #public methods
    def start(self):
        pass

    def changeScene(self, scene):
        pass


    def getLevel(self):
        pass


    def getScore(self):
        pass

    def increaseScore(self, score):
        pass

    def getLives(self):
        pass

    def getBalls(self):
        pass

    def getPad(self):
        pass

    def playSound(self, soundClip):
        pass

    def reduceLives(self):
        pass

    def increaseLives(self):
        pass

    def reset(self):
        pass



    #main
Breakout().start()


