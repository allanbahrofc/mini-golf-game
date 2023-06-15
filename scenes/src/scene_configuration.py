from dotenv import load_dotenv
import os

env = load_dotenv('../../.env')

config = {
    'width': int(os.environ.get('width')),
    'height': int(os.environ.get('height'))
}

colors = {
    'lightGreen': (113,247,159),
    'lightSalmon': (243,211,189),
    'lightPurple': (139,114,142),
    'darkGreen': (74,124,89),
    'darkPurple': (34,3,31)
}

sprites = {
    'ballOneSprite': '../res/sprites/Ball1.png',
    'holeOneSprite': '../res/sprites/Hole1.png',
    'holeTwoSprite': '../res/sprites/Ball2.png',
    'holeTwoSprite': '../res/sprites/Hole2.png',
}
walls = {
    'background': '../res/tiles/background.png',
    'topSideWall': '../res/tiles/wallTopSide.png',
    'leftSideWall': '../res/tiles/wallLeftSide.png',
    'RightSideWall': '../res/tiles/wallRightSide.png',
    'leftTopSideWall': '../res/tiles/wallTopLeft.png',
    'rightTopSideWall': '../res/tiles/wallTopRight.png',
    'bottomSideWall': '../res/tiles/wallBottomSide.png',
    'leftBottomSideWall': '../res/tiles/wallBottomLeft.png',
    'rightBottomSideWall': '../res/tiles/wallBottomRight.png',
}
