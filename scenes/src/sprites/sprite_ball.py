from scene_configuration import sprites, config, colors
import pyglet
class Ball(pyglet.sprite.Sprite):
    def __init__(self, img, x=0, y=0):
        self.image = img
        self.x = x
        self.y = y
