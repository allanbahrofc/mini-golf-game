import pyglet
import dotenv
import os
dotenv.load_dotenv('.env')
WIDTH = os.environ.get('WIDTH')
HEIGHT = os.environ.get('HEIGHT')

windowGame = pyglet.window.Window()
windowGame.width = WIDTH
windowGame.height = HEIGHT

@windowGame.event
def on_draw():
    windowGame.clear()

pyglet.app.run(60)