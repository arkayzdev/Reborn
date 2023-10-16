from service.scraping.arena import AreNaService 
from service.scraping.pinterest import PinterestService 
from service.scraping.savee import SaveeItService 

class SearchService:
    def pinterest(self, search: str) -> list:
        pin = PinterestService()
        research_page = pin.search_parser(search)
        links = pin.get_links(research_page)
        images =  pin.get_all_img(links)   
        return images
    
    def arena(self, search: str) -> list:
        arena = AreNaService()
        research_page = arena.search_parser(search)
        links = arena.get_links(research_page)
        images =  arena.get_all_img(links)   
        return images
    
    def savee(self, search: str) -> list:
        savee = SaveeItService()
        research_page = savee.search_parser(search)
        links = savee.get_links(research_page)
        print(links)
        images =  savee.get_all_img(links)   
        return images
        
test = SearchService()
print(test.pinterest("gojo satoru"))