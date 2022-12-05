from flask import Flask
from Config import Config

Bryant = Flask(__name__)
Bryant.config.from_object(Config)
