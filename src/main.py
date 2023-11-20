
from selectolax.parser import HTMLParser

from scraper.rei import ReiSpider
from scraper.debug import ReiSpiderDebug



def main():
    spider: ReiSpider = ReiSpider()
    spider.get_product_detail(url="https://www.rei.com/product/216094/baffin-young-eiger-snow-boots-kids?color=CHARCOAL/BLUE")

def debug():
    spider: ReiSpiderDebug = ReiSpiderDebug()
    with open("response_detail.html", "r", encoding="UTF-8") as html_file:
        soup = HTMLParser(html=html_file.read())
        spider.get_product_detail(soup=soup)

if __name__ == "__main__":
    debug()