from selectolax.parser import HTMLParser

from scraper.rei import ReiSpider
from scraper.debug import ReiSpiderDebug


from scraper.command.cli import app as cli_app


def main():
    spider: ReiSpider = ReiSpider()
    spider.get_product_list(search_query="shoes")


def debug():
    spider: ReiSpiderDebug = ReiSpiderDebug()
    with open("search_response.html", "r", encoding="UTF-8") as html_file:
        soup = HTMLParser(html=html_file.read())
        spider.get_product_items(soup=soup)


if __name__ == "__main__":
    cli_app(prog_name="main")
