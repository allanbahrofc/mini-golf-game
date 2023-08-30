import entity.entityPlayer as entityPlayerBehavior
import entity.entityHole as entityHoleBehavior
import enviroment.wallBackground as enviromentWallBg
import config
import pygame

# (Init)
pygame.init()
pygame.joystick.init()
pygame.joystick.get_init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
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
wallsGroup = pygame.sprite.Group()
playerBehavior = entityPlayerBehavior.entityPlayer()
holeBehavior = entityHoleBehavior.entityHole()
wallBackground = enviromentWallBg.wallBackground(20,20)

wallsGroup.add(wallBackground)
entityGroup.add(playerBehavior)
obstacleGroup.add(holeBehavior)

fontScreen = pygame.font.SysFont("Arial Black", 20)
# (Loop)
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    holesFont = fontScreen.render(f"Hole {playerBehavior.score}", True, config.colors['darkGreen'])
    displayScreen.fill(config.colors['darkGreen2'])
    if holeBehavior.rect.colliderect(playerBehavior):
        holeBehavior.respawnHole()
        pygame.mixer.music.load('./audio/hole_one.wav')
        pygame.mixer.music.play()
        playerBehavior.score += 1
        playerBehavior.velocity += 0.25
    if playerBehavior.gameOver == True:
        isRunning = False
    displayScreen.blit(holesFont, (200,70))
    entityGroup.draw(displayScreen)
    obstacleGroup.draw(displayScreen)
    wallsGroup.draw(displayScreen)
    playerBehavior.update()
    wallsGroup.update()
    pygame.display.flip()
    clockFPS.tick(60)