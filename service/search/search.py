from service.scraping.are_na import AreNaService as arena
from service.scraping.pinterest import PinterestService as pin
from service.scraping.savee_it import SaveeItService as savee

class SearchService:
    def pinterest(self, search: str) -> list:
        research_page = pin.search_parser()
        links = pin.get_links(research_page)
        