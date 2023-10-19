from service.scrape.arena import AreNaService 
from service.scrape.pinterest import PinterestService 
from service.scrape.savee import SaveeItService
from service.scrape.scrape import ScrapeService 

class SearchService:
    def __init__(self) -> None:
        self.resources = []
        self.resources.append(PinterestService())
        self.resources.append(AreNaService())
        self.resources.append(SaveeItService())
        
    def search (self, search: str):
        all_img = list()
        resource: ScrapeService
        for resource in self.resources:
            research_page = resource.search_parser(search)
            links = resource.get_links(research_page)
            images =  resource.get_all_img(links)   
            all_img.append(images)
        return all_img

    
        
