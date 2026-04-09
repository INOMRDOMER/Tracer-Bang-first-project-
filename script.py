import pygame
import random
import time

pygame.init()

run = True

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tracer Bang")
clock = pygame.time.Clock()
fon = pygame.font.SysFont("Arial", 20)


speed = 8
sleep = False
ySpawn = 0
xSpawn = 0
x = 350
metres = 0
recordes = 0
timeSPAWN = 0
spawn = False
monster = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xSpawn, ySpawn, 60, 60))
help1 = fon.render(f"Слоумо: SPACE", True, (0, 0, 0))


while run:
    clock.tick(60)
    timeSPAWN += 1
    metres += 0.1
    metresF = int(metres)

    scoreMetres = fon.render(f"{metresF} Метров", True, (0, 0, 0))
    recordMetres = fon.render(f"Рекорд: {recordes}", True, (0, 0, 0))

    x = max(240, min(x, 500))



    screen.fill((63, 108, 4))
    screen.blit(scoreMetres, (0, 0))
    screen.blit(recordMetres, (650, 0))
    trace = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(240, 0, 320, 600))
    tracevisual = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(390, 0, 10, 600))
    player = pygame.draw.rect(screen, (25, 45, 68), pygame.Rect(x, 350, 60, 120))
    playervisual = pygame.draw.rect(screen, (25, 50, 90), pygame.Rect(x, 390, 60, 60))
    playerFARI1 = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, 350, 20, 5))
    playerFARI2 = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x + 40, 350, 20, 5))
    playerFARI3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, 465, 20, 5))
    playerFARI4 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x + 40, 465, 20, 5))
    screen.blit(help1, (0, 20))

    if timeSPAWN % 250 == 0:
        xSpawn = random.randint(250, 500)
        spawn = True



    if spawn:
        ySpawn += speed
        monster = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(xSpawn, ySpawn, 60, 60))
        if ySpawn > 1000:
            ySpawn = 0
            speed += 0.1

    if player.colliderect(monster):
      if metres > recordes:
         recordes = int(metres)
         metres = 0
         ySpawn = 0
         x = 350
         timeSPAWN = 0
         xSpawn = random.randint(250, 500)
      else:
         metres = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += 50
            if event.key == pygame.K_a:
                x -= 55
            if event.key == pygame.K_SPACE:
             if sleep:
                sleep = False
             else:
                sleep = True

    if sleep:
        time.sleep(0.1)

    pygame.display.flip()