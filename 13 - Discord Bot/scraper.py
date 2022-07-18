import requests
import re
from bs4 import BeautifulSoup

PATTERN = '<div class="profilLast">([^\s]+)'

def get_current_price(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    tag = doc.find_all("div", class_="profilLast")
    try:
        text_ = str(tag[0])
        price = re.findall(PATTERN, text_)
    except:
        return None
    else:
        return price[0]