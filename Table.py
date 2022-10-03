import numpy
import pygame
import Ball
import Color

class Table:
  def __init__(self, size, color, screen):
    sizeFactor = 500
    self.size = width, height = size[0] - sizeFactor, size[1] - sizeFactor
    self.screen = screen
    self.pos = x, y = sizeFactor / 2, sizeFactor / 2
    numOfBalls = 1
    self.balls = [
      Ball.Ball(pygame.Vector2(sizeFactor + 100, self.size[1] / 2 + self.pos[1]), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 20, self.size[1] / 2 + self.pos[1] + 10), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 20, self.size[1] / 2 + self.pos[1] - 10), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 40, self.size[1] / 2 + self.pos[1]), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 40, self.size[1] / 2 + self.pos[1] + 20), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 40, self.size[1] / 2 + self.pos[1] - 20), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 60, self.size[1] / 2 + self.pos[1] + 10), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 60, self.size[1] / 2 + self.pos[1] - 10), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 60, self.size[1] / 2 + self.pos[1] + 30), 10, Color.orange, screen),
      Ball.Ball(pygame.Vector2(sizeFactor + 100 + 60, self.size[1] / 2 + self.pos[1] - 30), 10, Color.orange, screen),
    ]

    self.balls.append(Ball.PlayerBall(pygame.Vector2(sizeFactor - 100, self.size[1] / 2 + self.pos[1]), 10, Color.white, screen))

  def Draw(self):
    pygame.draw.rect(self.screen, Color.brown, ((self.pos[0] - 20, self.pos[1] - 20), (self.size[0] + 40, self.size[1] + 40)))
    pygame.draw.rect(self.screen, Color.green, (self.pos, self.size))
  
  def CollisionWall(self):
    for ball in self.balls:
      if ball.pos.x < self.pos[0]:
        ball.vel = ball.vel.reflect(pygame.Vector2(1, 0))
      if ball.pos.x > self.pos[0] + self.size[0]:
        ball.vel = ball.vel.reflect(pygame.Vector2(-1, 0))
      if ball.pos.y < self.pos[1]:
        ball.vel = ball.vel.reflect(pygame.Vector2(0, 1))
      if ball.pos.y > self.pos[1] + self.size[1]:
        ball.vel = ball.vel.reflect(pygame.Vector2(0, -1))

  def Collision(self):
    for i in range(0, len(self.balls)):
      for j in range(i + 1, len(self.balls)):
        if self.balls[i].pos.distance_to(self.balls[j].pos) < self.balls[i].rad * 2:
          totVel = self.balls[i].vel + self.balls[j].vel
          dist = self.balls[i].pos - self.balls[j].pos
          dist.scale_to_length(totVel.length())
          self.balls[i].vel = self.balls[i].vel + dist
          self.balls[j].vel = self.balls[j].vel + dist * -1
          if self.balls[i].vel.length() > 0:
            self.balls[i].vel.scale_to_length(totVel.length() / 2)
          if self.balls[j].vel.length() > 0.002:
            self.balls[j].vel.scale_to_length(totVel.length() / 2)