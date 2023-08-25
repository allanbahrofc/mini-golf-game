import entity.entityPlayer as entityPlayerBehavior
import entity.entityHole as entityHoleBehavior
import config
import pygame

# (Init)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.font.init()
pygame.font.get_init()

# (Default)
titleScreen = pygame.display.set_caption('Mini Golf')
clockFPS = pygame.time.Clock()
displayScreen = pygame.display.set_mode(
    [config.window['width'], config.window['height']])

# (Prefab)
entityGroup = pygame.sprite.Group()
obstacleGroup = pygame.sprite.Group()
playerBehavior = entityPlayerBehavior.entityPlayer()
holeBehavior = entityHoleBehavior.entityHole()

entityGroup.add(playerBehavior)
obstacleGroup.add(holeBehavior)

holesQntd = 0
fontScreen = pygame.font.SysFont("Arial Black", 20)
# (Loop)
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    holesFont = fontScreen.render(f"Hole {holesQntd}", True, config.colors['lightPurple'])
    displayScreen.fill(config.colors['darkPurple'])
    if holeBehavior.rect.colliderect(playerBehavior):
        holeBehavior.respawnHole()
        pygame.mixer.music.load('./audio/hole_one.wav')
        pygame.mixer.music.play()
        holesQntd += 1
    if playerBehavior.gameOver == True:
        isRunning = False
    displayScreen.blit(holesFont, (200,70))
    entityGroup.draw(displayScreen)
    obstacleGroup.draw(displayScreen)
    playerBehavior.update()
    pygame.display.flip()
    clockFPS.tick(60)