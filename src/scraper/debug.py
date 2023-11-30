import json


from rich import print
from selectolax.parser import HTMLParser
from typing import Any

from scraper.utils.validation import Validation


class ReiSpiderDebug(object):
    def __init__(self, validation: Validation = Validation()):
        self.validation: Validation = validation
        self.base_url: str = "https://www.rei.com"

    def get_product_detail(self, soup: HTMLParser) -> dict[str, Any]:
        # data mentah
        scripts = soup.css_first("script#modelData")

        # teknik parsing
        datas = self.get_data_from_json(scripts.text())
        return datas

    def get_product_items(self, soup: HTMLParser) -> list[str]:
        urls: list[str] = []
        search_items = soup.css_first("div#search-results")
        products = search_items.css("ul.cdr-grid_13-5-2 > li")
        for product in products:
            product_url = product.css_first("a").attributes.get("href")
            urls.append(self.base_url + product_url)

        # cetak urls yang ditemukan disini
        print("Total Product URL's Found: {}".format(len(urls)))
        return urls

    def get_pages_number(self, soup: HTMLParser) -> int:
        pages = soup.css_first('a[data-id="pagination-test-link"]').text()
        return self.validation.is_valid_pages_number(pages)

    def get_data_from_json(self, obj: str):
        data_dict: dict[str, Any] = {}
        datas = json.loads(obj)

        # proses parsing JSON
        product = datas["pageData"]["product"]
        product_url = self.base_url + product["canonicalUrl"]
        product_sizes = product["sizes"]
        product_specs = product["techSpecs"]
        product_size_chart = product["sizeChart"]
        product_images = product["images"]
        product_price = product["availablePrices"]
        product_skus = product["skus"]
        product_feature = product["features"]
        product_color = product["byColor"]

        phone_number = datas["openGraphProperties"]["og:phone_number"]

        # proses untuk tambah data
        data_dict["title"] = datas["title"]
        data_dict["phone_number"] = self.validation.is_valid_phone(phone_number)
        data_dict["product_url"] = product_url
        data_dict["product_size"] = product_sizes
        data_dict["product_specifications"] = product_specs
        data_dict["product_size_chart"] = product_size_chart
        data_dict["product_image"] = product_images
        data_dict["product_price"] = product_price
        data_dict["product_sku"] = product_skus
        data_dict["product_feature"] = product_feature
        data_dict["product_color"] = product_color

        return data_dict
