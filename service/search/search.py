from service.scrape.arena import AreNaService 
from service.scrape.pinterest import PinterestService 
from service.scrape.savee import SaveeItService
from service.scrape.scrape import ScrapeService 

class SearchService:
    def __init__(self) -> None:
        self.resources = dict()
        self.resources['pinterest'] = PinterestService()
        self.resources['arena'] = AreNaService()
        self.resources['savee'] = SaveeItService()
        

    def search_all (self, search: str):
        all_img = list()
        resource: ScrapeService
        for resource in self.resources.values():
            research_page = resource.search_parser(search)
            links = resource.get_links(research_page)
            images =  resource.get_all_img(links)   
            all_img.append(images)
        return all_img


    def search_one(self, search: str, website: str):
        all_img = list()
        resource: ScrapeService
        for key, resource in self.resources.items():
            if key == website :
                research_page = resource.search_parser(search)
                links = resource.get_links(research_page)
                images =  resource.get_all_img(links)   
                all_img.append(images)
        return all_img
        
