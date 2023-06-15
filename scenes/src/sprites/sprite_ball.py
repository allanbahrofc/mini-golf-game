import pyglet

class Ball(pyglet.sprite.Sprite):
    def __init__(self, img, x=0, y=0):
        super().__init__(img, x, y)

