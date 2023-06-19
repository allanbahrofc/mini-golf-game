from scene_configuration import config, colors, sprites, walls
import pyglet

# Display
displayWidth = config['width']
displayHeight = config['height']
display = pyglet.window.Window(displayWidth, displayHeight)
display.set_caption('Mini Golf')

# Sprites
ballSprite = pyglet.image.load(sprites['ballOneSprite'])
ball = pyglet.sprite.Sprite(ballSprite, 0, 0)
background = pyglet.shapes.Rectangle(0,0,displayWidth,displayHeight,colors['lightGreen'])

@display.event
def on_draw():
    display.clear()
    background.draw()
    ball.draw()
pyglet.app.run()

#TODO
# Make Graphics