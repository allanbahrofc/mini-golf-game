from scene_configuration import config
import pyglet

# ---
# Display
# ---
displayWidth = config['width']
displayHeight = config['height']
display = pyglet.window.Window(displayWidth, displayHeight)
display.set_caption('Mini Golf')

# ---
# Colors
# ---
greenColor = (255,0,0)
blackColor = (0,0,0)

# ---
# Sprites
# ---
background = pyglet.shapes.Rectangle(0,0,displayWidth,displayHeight,greenColor)

@display.event
def on_draw():
    display.clear()
    background.draw()
pyglet.app.run()

#TODO
# Make Graphics