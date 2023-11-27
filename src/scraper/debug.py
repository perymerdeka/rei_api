import json


from rich import print
from selectolax.parser import HTMLParser
from typing import Any

from scraper.utils.validation import Validation

class ReiSpiderDebug(object):
    def __init__(self, validation: Validation = Validation()):
        self.validation = validation

    def get_product_detail(self, soup: HTMLParser):
        # data mentah
        scripts = soup.css_first("script#modelData")
        
        # teknik parsing
        datas = self.get_data_from_json(scripts.text())
        print(datas)


    def get_data_from_json(self,  obj: str):
        data_dict: dict[str, Any] = {}
        datas = json.loads(obj)

        # proses parsing JSON
        
        phone_number = datas["openGraphProperties"]['og:phone_number']

        # proses untuk tambah data
        data_dict['title'] = datas['title']
        data_dict['phone_number'] = self.validation.is_valid_phone(phone_number)
        return data_dict