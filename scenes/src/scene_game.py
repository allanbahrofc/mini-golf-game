from scene_configuration import config, colors, sprites, walls
import pyglet

# ---
# Display
# ---
displayWidth = config['width']
displayHeight = config['height']
display = pyglet.window.Window(displayWidth, displayHeight)
display.set_caption('Mini Golf')

# ---
# Sprites
# ---
background = pyglet.shapes.Rectangle(0,0,displayWidth,displayHeight,colors['greenColor'])

@display.event
def on_draw():
    display.clear()
    background.draw()
pyglet.app.run()

#TODO
# Make Graphics