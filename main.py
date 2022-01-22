#https://docs-python.ru/standart-library/modul-platform-python/
#https://cryptoworld.su/sbor-informacii-o-sisteme-s-python/
from flask import Flask
import platform
import getpass
import os
import socket
import psutil

app = Flask(__name__)

@app.route('/')
def hello():
    info = (platform.platform(), platform.processor())
    return info[1]

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
