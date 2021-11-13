import requests
import re
import ctypes
import random
import time
import os


def main(url):
    response = get_response(url)
    pic_urls = get_urls(response)
    change_wallpaper(pic_urls)


def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def get_urls(response):
    pic_matches = re.findall('"display_url":"([^"]+)"', response)
    return list({match.replace("\\u0026", "&") for match in pic_matches})


def image_handler(image_url):
    img_data = requests.get(image_url).content
    with open('wallpaper.jpg', 'wb') as handler:
        handler.write(img_data)


def change_wallpaper(pic_urls):
    WALLPAPER_PATH = get_wallpaper_path()
    while True:
        image_handler(random.choice(pic_urls))
        ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH , 0)
        time.sleep(3)


def get_wallpaper_path():
    path = os.getcwd()
    path = path.replace('\\', '/')
    path += "/wallpaper.jpg"
    return path

main("https://www.instagram.com/lx_offiziell/")
