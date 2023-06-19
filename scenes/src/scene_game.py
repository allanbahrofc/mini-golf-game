from scene_configuration import config, colors, sprites, walls
from sprites.sprite_ball import Ball
import pyglet

# Display
displayWidth = config['width']
displayHeight = config['height']
display = pyglet.window.Window(displayWidth, displayHeight)
display.set_caption('Mini Golf')

# Sprites
Ball(pyglet.image.load(sprites['ballOneSprite']),0, 0)
background = pyglet.shapes.Rectangle(0,0,displayWidth,displayHeight,colors['lightGreen'])

@display.event
def on_draw():
    display.clear()
    background.draw()
    Ball.draw()
pyglet.app.run()

#TODO
# Make Graphics