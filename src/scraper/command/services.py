from scraper.runner import Runner
from scraper.extractor import Extract


class ScraperCommandService(object):
    def __init__(self) -> None:
        self.runner: Runner = Runner()
        self.extract: Extract = Extract()

    def scrape(self, search_query: str):
        self.runner.generate_all_products(search_query=search_query)
    
    def spesific_scrape(self):
        pass