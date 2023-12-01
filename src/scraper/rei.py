import httpx
import json


from typing import Any, Optional
from selectolax.parser import HTMLParser
from rich import print

from scraper.utils.validation import Validation


class ReiSpider(object):
    def __init__(self, validation: Validation = Validation()):
        self.validation: Validation = validation
        self.base_url: str = "https://www.rei.com"

    def get_pages_number(self, soup: HTMLParser) -> int:
        """fungsi untuk mendapatkan total halaman

        Args:
            soup (HTMLParser): soup object

        Returns:
            int: total halaman
        """

        pages = soup.css_first('a[data-id="pagination-test-link"]').text()
        return self.validation.is_valid_pages_number(pages)
    
    def get_product_detail(self, soup: HTMLParser) -> dict[str, Any]:
        """fungsi untuk mendapatkan product detail

        Args:
            soup (HTMLParser): soup object

        Returns:
            dict[str, Any]: detail product yang sudah di parsing
        """
        # data mentah
        scripts = soup.css_first("script#modelData")

        # teknik parsing
        datas = self.get_data_from_json(scripts.text())
        return datas

    def get_data_from_json(self, obj: str) -> dict[str, Any]:
        """fungsi untuk parsing product dari JSON

        Args:
            obj (str): soup Object

        Returns:
            dict[str, Any]: data product yang sudah di parsing
        """

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

    
    def get_product_items(self, soup: HTMLParser) -> list[str]:
        """Fungsi Untuk mendapatkan semua link product dalam satu halaman

        Args:
            soup (HTMLParser): soup object

        Returns:
            list[str]: kumpulan url product untuk dilakukan scrape
        """
        urls: list[str] = []
        search_items = soup.css_first("div#search-results")
        products = search_items.css("ul.cdr-grid_13-5-2 > li")
        for product in products:
            product_url = product.css_first("a").attributes.get("href")
            urls.append(self.base_url + product_url)

        # cetak urls yang ditemukan disini
        print("Total Product URL's Found: {}".format(len(urls)))
        return urls

    def get_product_list(self, search_query: str = "", page_number: Optional[str] = "") -> list[dict[str, Any]]:
        """fungsi untuk mendapatkan daftar product per halaman

        Args:
            search_query (str, optional): Kata Kunci Untuk Mencari Product. Defaults to "".
            page_number (Optional[str], optional): Nomor Halaman. Defaults to "".

        Returns:
            list[dict[str, Any]]: Product data pada 1 halaman
        """
        products: list[dict[str, Any]] = []
        if page_number == "":
            url: str = self.base_url + "/search?q={}".format(search_query)
        else:
            url: str = self.base_url + "/search?q={}&page={}".format(
                search_query, page_number
            )

        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        response = httpx.get(url=url, headers=headers)

        # olah response
        f = open("search_response.html", "w+", encoding="UTF-8")
        f.write(response.text)
        f.close()

        soup: HTMLParser = HTMLParser(response.text)

        products_list = self.get_product_items(soup=soup)
        for product in products_list:
            product_data = self.get_product_data(url=product)
            products.append(product_data)

        # proses product disini

        return products


    def get_product_data(self, url: str) -> dict[str, Any]:
        """fungsi untuk mendapatkan product dengan URL

        Args:
            url (str): URL Product

        Returns:
            dict[str, Any]: detail Product yang sudah di parsing
        """


        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        # olah response
        response = httpx.get(url=url, headers=headers)

        # langkah sesudah mendapatkan data
        f = open("response_detail.html", "w+", encoding="UTF-8")
        f.write(response.text)
        f.close()

        soup: HTMLParser = HTMLParser(response.text)

        # ambil data disini
        product = self.get_product_detail(soup=soup)

        # return hasilnya
        return product

   