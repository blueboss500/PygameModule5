import pygame
from Game.Scenes import Scene

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        #pass event to base class
        super(PlayingGameScene, self).handleEvents(events)

        #specific scene event handling
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        balls = game.getBalls()
        pad = game.getPad()

        for ball in balls:
            
            #check if balls intersect each other
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                ball.changeDirection(pad)

            ball.updatePosition()

            game.screen.blit(ball.getSprite(), ball.getPosition())
            
        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        
        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())
