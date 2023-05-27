import dotenv
import os

dotenv.load_dotenv('/.env')

config = {
    "width": os.environ.get('width'),
    "height": os.environ.get('height')
}