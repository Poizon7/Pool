import sys, pygame
import Table
import Color

class Game:
  p1Score = 0
  p2Score = 0
  size = width, height = 1920, 1080

  def Run(self):
    pygame.init()

    screen = pygame.display.set_mode(self.size)
    table = Table.Table(self.size, Color.green, screen)
    
    GAME_FONT = pygame.freetype.SysFont("Times New Roman", 48)

    while 1:
      if len(table.balls) == 1:
        break
      for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if (True, False, False) == pygame.mouse.get_pressed(): table.balls[len(table.balls) - 1].Shoot()
      screen.fill(Color.black)
      GAME_FONT.render_to(screen, (0, 0), str(self.p1Score), Color.white)
      GAME_FONT.render_to(screen, (self.size[0] - 20, 0), str(self.p2Score), Color.white)
      table.Draw()
      table.CollisionWall()
      table.Collision()
      for ball in table.balls:
        ball.Move()
        ball.Draw()
      table.balls[len(table.balls) - 1].ShootingLine()
      pygame.display.flip()