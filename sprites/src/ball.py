import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('./res/ball_golf.png')
        self.pos = pygame.Vector2()
        self.pos.xy = [0, 0]

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]):
            self.pos.x -= 1
        elif (keys[pygame.K_UP]):
            self.pos.y -= 1
        elif (keys[pygame.K_DOWN]):
            self.pos.y += 1
        elif (keys[pygame.K_RIGHT]):
            self.pos.x += 1

    def draw(self, surface):
        surface.blit(self.image, (self.pos.x, self.pos.y))

    def delete(self):
        self.kill()
