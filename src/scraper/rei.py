import httpx


from typing import Any
from selectolax.parser import HTMLParser
from rich import print



class ReiSpider(object):
    def __init__(self)-> None:
        pass

    def get_product_detail(self, url: str):
        headers: dict[str, Any] = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
        response = httpx.get(url=url, headers=headers)

        # langkah sesudah mendapatkan data
        f = open("response_detail.html", 'w+', encoding="UTF-8")
        f.write(response.text)
        f.close()

        soup: HTMLParser = HTMLParser(response.text)

        # data mentah
        scripts = soup.css_first("script#modelData")

        # scraping proses / olah data
