from typing import Optional, Any

from scraper.rei import ReiSpider

class Runner(object):
    def __init__(self) -> None:
        self.spider: Optional[ReiSpider] = ReiSpider()
    
    def get_spesific_pages(self, search_query: str, page_number: Optional[str]="") -> list[dict[str, Any]]:
        products = self.spider.get_product_list(search_query=search_query, page_number=page_number)
        return products