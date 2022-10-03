import sys, pygame
import Table
import Color

class Game:
  p1Score = 0
  p2Score = 0
  size = width, height = 1080, 720

  def Run(self):
    pygame.init()

    screen = pygame.display.set_mode(self.size)
    table = Table.Table(self.size, Color.green, screen)

    while 1:
        for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()
          if (True, False, False) == pygame.mouse.get_pressed(): table.balls[len(table.balls) - 1].Shoot()
        screen.fill(Color.black)
        table.Draw()
        table.CollisionWall()
        table.Collision()
        for ball in table.balls:
          ball.Move()
          ball.Draw()
        table.balls[len(table.balls) - 1].ShootingLine()
        pygame.display.flip()