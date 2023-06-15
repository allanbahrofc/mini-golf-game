from dotenv import load_dotenv
import os

env = load_dotenv('../../.env')

config = {
    'width': int(os.environ.get('width')),
    'height': int(os.environ.get('height'))
}

colors = {
    'background': (255, 220, 00)
}

sprites = {
    'ball': '',
    'hole': ''
}
walls = {
    'background': '',
    'leftTopSideWall': '',
}
