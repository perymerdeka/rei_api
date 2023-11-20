
from rich import print
from selectolax.parser import HTMLParser

class ReiSpiderDebug(object):
    def __init__(self):
        pass

    def get_product_detail(self, soup: HTMLParser):
        # data mentah
        scripts = soup.css_first("script#modelData")
        print(scripts.html)