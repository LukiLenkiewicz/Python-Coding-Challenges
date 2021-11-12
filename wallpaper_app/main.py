import requests
import re
import ctypes
import random
import time
import os




def name():
    pass


def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})


def image_handler(image_url):
    print(image_url)
    img_data = requests.get(image_url).content
    with open('wallpaper.jpg', 'wb') as handler:
        handler.write(img_data)


def get_wallpaper_path():
    path = os.getcwd()
    path = path.replace('\\', '/')
    path += "/wallpaper.jpg"
    return path

url = "https://www.instagram.com/lx_offiziell/"
response = get_response(url)

pic_matches = re.findall('"display_url":"([^"]+)"', response)
pic_urls = prepare_urls(pic_matches)

WALLPAPER_PATH = get_wallpaper_path()

while True:
    image_handler(random.choice(pic_urls))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH , 0)
    time.sleep(3)