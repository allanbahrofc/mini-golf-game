import pyglet
from pyglet.gl import GL_ONE_MINUS_SRC_ALPHA, GL_SRC_ALPHA

class Ball(pyglet.sprite.Sprite):
    def __init__(self, img, x=0, y=0, z=0, blend_src=..., blend_dest=..., batch=None, group=None, subpixel=False):
        super().__init__(img, x, y, z, blend_src, blend_dest, batch, group, subpixel)

        