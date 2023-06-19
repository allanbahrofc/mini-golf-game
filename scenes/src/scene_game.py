from scene_configuration import config, colors, sprites, walls,keys
import pyglet


# Display
displayWidth = config['width']
displayHeight = config['height']
display = pyglet.window.Window(displayWidth, displayHeight)
display.set_caption('Mini Golf')

# Sprites
ballSprite = pyglet.image.load(sprites['ballOneSprite'])
background = pyglet.shapes.Rectangle(0,0,displayWidth,displayHeight,colors['lightGreen'])

# Instancies
ball = pyglet.sprite.Sprite(ballSprite, 0, 0)

@display.event
def on_draw():
    display.clear()
    background.draw()
    ball.draw()

@display.event
def on_key_press(symbol, modifiers):
    if(symbol == keys['upArrow']):
        print('going up to the sky')
    elif(symbol == keys['downArrow']):
        print('going down to the ground')
    elif(symbol == keys['leftArrow']):
        print('going to the left')
    elif(symbol == keys['rightArrow']):
        print('going to the right')
pyglet.app.run()

#TODO
# Make Graphics