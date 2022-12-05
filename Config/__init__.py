import os


class Config:
    ROOT = os.getcwd()
    LOG_NAME = os.path.join(ROOT, 'logs', 'Bryant.log')
