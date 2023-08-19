import entity.entityPlayer as entityPlayerBehavior
import entity.entityHole as entityHoleBehavior
import config
import pygame

# (Init)
pygame.init()
pygame.mixer.music.load('')
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

# (Loop)
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    displayScreen.fill(config.colors['darkGreen'])
    if holeBehavior.rect.colliderect(playerBehavior):
        holeBehavior.respawnHole()
    entityGroup.draw(displayScreen)
    obstacleGroup.draw(displayScreen)
    playerBehavior.update()
    pygame.display.flip()
    clockFPS.tick(60)
