from service.scraping.arena import AreNaService 
from service.scraping.pinterest import PinterestService 
from service.scraping.savee import SaveeItService
from service.scraping.scraping import ScrapingService 

class SearchService:
    def __init__(self) -> None:
        self.resources = []
        self.resources.append(PinterestService())
        self.resources.append(AreNaService())
        self.resources.append(SaveeItService())
        
    def search (self, search: str):
        all_img = list()
        resource: ScrapingService
        for resource in self.resources:
            research_page = resource.search_parser(search)
            links = resource.get_links(research_page)
            images =  resource.get_all_img(links)   
            all_img.append(images)
        return all_img

    
        
