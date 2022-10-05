import numpy
import pygame
import Ball
import Color

class Table:
  def __init__(self, size, color, screen):
    self.screenSize = size
    self.size = width, height = 600, 250
    self.screen = screen
    self.pos = x, y = (size[0] - width) / 2, (size[1] - height) / 2

    middleOfScreenX = size[0] / 2
    middleOfScreenY = size[1] / 2
    ballOffsetX = 100
    ballOffsetFactorX = 20
    ballOffsetFactorY = 10
    self.balls = [
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX, middleOfScreenY), 10, Color.orange, screen),

      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + ballOffsetFactorX, middleOfScreenY + ballOffsetFactorY), 10, Color.red, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + ballOffsetFactorX, middleOfScreenY - ballOffsetFactorY), 10, Color.red, screen),

      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 2 * ballOffsetFactorX, middleOfScreenY), 10, Color.black, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 2 * ballOffsetFactorX, middleOfScreenY + 2 * ballOffsetFactorY), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 2 * ballOffsetFactorX, middleOfScreenY - 2 * ballOffsetFactorY), 10, Color.red, screen),

      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 3 * ballOffsetFactorX, middleOfScreenY + ballOffsetFactorY), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 3 * ballOffsetFactorX, middleOfScreenY - ballOffsetFactorY), 10, Color.red, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 3 * ballOffsetFactorX, middleOfScreenY + 3 * ballOffsetFactorY), 10, Color.red, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 3 * ballOffsetFactorX, middleOfScreenY - 3 * ballOffsetFactorY), 10, Color.orange, screen),

      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 4 * ballOffsetFactorX, middleOfScreenY), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 4 * ballOffsetFactorX, middleOfScreenY + 2 * ballOffsetFactorY), 10, Color.red, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 4 * ballOffsetFactorX, middleOfScreenY - 2 * ballOffsetFactorY), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 4 * ballOffsetFactorX, middleOfScreenY + 4 * ballOffsetFactorY), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(middleOfScreenX + ballOffsetX + 4 * ballOffsetFactorX, middleOfScreenY - 4 * ballOffsetFactorY), 10, Color.red, screen),
    ]

    self.balls.append(Ball.PlayerBall(pygame.Vector2(middleOfScreenX - ballOffsetX, middleOfScreenY), 10, Color.white, screen))

  def Draw(self):
    pygame.draw.rect(self.screen, Color.brown, ((self.pos[0] - 20, self.pos[1] - 20), (self.size[0] + 40, self.size[1] + 40)))
    for i in range(0, 3):
      pygame.draw.circle(self.screen, Color.black, (self.pos[0] + i * self.size[0] / 2, self.pos[1]), 15)
    for i in range(0, 3):
      pygame.draw.circle(self.screen, Color.black, (self.pos[0] + i * self.size[0] / 2, self.pos[1] + self.size[1]), 15)
    pygame.draw.rect(self.screen, Color.green, (self.pos, self.size))
  
  def CollisionWall(self):
    for ball in self.balls:
      if ball.pos.x - 10 < self.pos[0]:
        if ball.pos.y < self.pos[1] + 15 or ball.pos.y > self.pos[1] + self.size[1] - 15:
          self.RemoveBall(ball)
        else:
          ball.vel = ball.vel.reflect(pygame.Vector2(1, 0))
      if ball.pos.x + 10 > self.pos[0] + self.size[0]:
        if ball.pos.y < self.pos[1] + 15 or ball.pos.y > self.pos[1] + self.size[1] - 15:
          self.RemoveBall(ball)
        else:
          ball.vel = ball.vel.reflect(pygame.Vector2(-1, 0))
      if ball.pos.y - 10 < self.pos[1]:
        if ball.pos.x + 10 < self.pos[0] + 15 or ball.pos.x > self.pos[0] + self.size[0] - 15 or (ball.pos.x > self.pos[0] + self.size[0] / 2 - 15 and ball.pos.x < self.pos[0] + self.size[0] / 2 + 15):
          self.RemoveBall(ball)
        else:
          ball.vel = ball.vel.reflect(pygame.Vector2(0, 1))
      if ball.pos.y + 10 > self.pos[1] + self.size[1]:
        if ball.pos.x + 10 < self.pos[0] + 15 or ball.pos.x > self.pos[0] + self.size[0] - 15 or (ball.pos.x > self.pos[0] + self.size[0] / 2 - 15 and ball.pos.x < self.pos[0] + self.size[0] / 2 + 15):
          self.RemoveBall(ball)
        else:
          ball.vel = ball.vel.reflect(pygame.Vector2(0, -1))

  def RemoveBall(self, ball):
    if ball.color == Color.white:
      ball.pos = pygame.Vector2(self.screenSize[0] / 2 - 100, self.size[1] / 2 + self.pos[1])
      ball.vel = pygame.Vector2(0, 0)
    else:
      self.balls.remove(ball)

  def Collision(self):
    for i in range(0, len(self.balls)):
      for j in range(i + 1, len(self.balls)):
        if self.balls[i].pos.distance_to(self.balls[j].pos) < self.balls[i].rad * 2:
          totVel = self.balls[i].vel + self.balls[j].vel
          dist = self.balls[i].pos - self.balls[j].pos
          dist.scale_to_length(totVel.length() * 0.5)
          self.balls[i].vel = self.balls[i].vel + dist
          self.balls[j].vel = self.balls[j].vel + dist * -1
          if self.balls[i].vel.length() > 0:
            self.balls[i].vel.scale_to_length(totVel.length() / 2)
          if self.balls[j].vel.length() > 0.002:
            self.balls[j].vel.scale_to_length(totVel.length() / 2)