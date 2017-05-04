from os.path import join, dirname
import os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOSTNAME = os.environ.get("HOSTNAME")
PORT = int(os.environ.get("PORT", 4333))