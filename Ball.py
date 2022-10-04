import pygame
import pygame.freetype
import Color

class Ball:
  def __init__(self, pos, rad, color, screen):
    self.pos = pos
    self.vel = pygame.Vector2(0, 0)
    self.rad = rad
    self.color = color
    self.screen = screen
  
  def Draw(self):
    pygame.draw.circle(self.screen, self.color, self.pos, self.rad)

  def Move(self):
    if self.vel.length() > 0:
      length = self.vel.length() - 0.001
      if length < 0:
        length = 0
      self.vel.scale_to_length(length)
    self.pos = self.pos + self.vel

class PlayerBall(Ball):
  def ShootingLine(self):
    if self.vel.length() == 0: 
      mouse = pygame.Vector2(pygame.mouse.get_pos())
      pygame.draw.line(self.screen, Color.white, self.pos, mouse)
      GAME_FONT = pygame.freetype.SysFont("Times New Roman", 24)
      GAME_FONT.render_to(self.screen, mouse + pygame.Vector2(20, 0), str(pygame.Vector2(self.pos - mouse).length().__round__()), Color.white)
  def Shoot(self):
    if self.vel.length() == 0:
      self.vel = pygame.Vector2(self.pos - pygame.mouse.get_pos()) / 100
