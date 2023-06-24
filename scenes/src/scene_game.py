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
moving = False
# Instancies
ball = pyglet.sprite.Sprite(ballSprite, displayWidth/2, displayHeight/2)
tick = pyglet.clock.Clock()
@display.event
def on_draw():
    display.clear()
    background.draw()
    ball.draw()

@display.event
def on_key_press(symbol, modifiers):
    if(symbol == keys['upArrow']):
        direction = 'up'
    elif(symbol == keys['downArrow']):
        direction = 'down'
    elif(symbol == keys['leftArrow']):
        direction = 'left'
    elif(symbol == keys['rightArrow']):
        direction = 'right'
    else:
        direction = ''
    
    match direction:
        case 'up':
            ball.y += 1 * 2
        case 'down':
            ball.y -= 1 * 2
        case 'left':
            ball.x -= 1 * 2
        case 'right':
            ball.x += 1 * 2
pyglet.app.run(60/1000)
#TODO
# Make Graphics