import pygame
from Game.Scenes import Scene
from Game.Shared import *

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        if game.getLives() <= 0:
            game.changeScene(GameConstants.GAMEOVER_SCENE)

        balls = game.getBalls()
        ship = game.getShip()

        #render balls
        for ball in balls:
            #check if balls intersect each other
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    brick.hit()
                    game.increaseScore(brick.getHitPoints())
                    #ball.changeDirection(brick)
                    #When ball hits brick, ball should reinitialize..reset to fire again
                    ball.setPosition(((pygame.mouse.get_pos()[0] - 10), ship.getPosition()[1]))
                    ball.setMotion(0)
                    break

            if ball.intersects(ship):
                ball.changeDirection(ship)

            ball.updatePosition()

            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLives()

            game.screen.blit(ball.getSprite(), ball.getPosition())
        
        #render bricks
        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        #render ship
        ship.setPosition((pygame.mouse.get_pos()[0], ship.getPosition()[1]))
        game.screen.blit(ship.getSprite(), ship.getPosition())


        #render hi score
        self.clearText()
        self.addText("Your Score: " + str(game.getScore()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 60, 
                     size = 30)

        self.addText("Lives: " + str(game.getLives()),
                      x = 0,
                      y = GameConstants.SCREEN_SIZE[1] - 30, 
                      size = 30)

    def handleEvents(self, events):
        #pass event to base class
        super(PlayingGameScene, self).handleEvents(events)

        #specific scene event handling
        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(1)