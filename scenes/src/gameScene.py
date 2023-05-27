import pyglet
import settings

windowGame = pyglet.window.Window()
windowGame.width = settings.config['width']
windowGame.height = settings.config['height']

@windowGame.event
def on_draw():
    windowGame.clear()

pyglet.app.run(60)