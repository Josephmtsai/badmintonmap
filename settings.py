# settings.py
from os.path import join, dirname
import dotenv

dotenv_path = join(dirname(__file__), '.env')
dotenv.load(dotenv_path)