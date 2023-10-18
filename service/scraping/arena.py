from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from model.image import Image
from service.scraping.scraping import ScrapingService
import queue
import threading

class AreNaService(ScrapingService):
    def search_parser(self, search: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            
            page.goto(f"https://www.are.na/search/{search}/blocks?block_filter=IMAGE")

            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html
    

    def get_links(self, html):
        div_links = html.select('a[href^="/block/"]')
        img_links = [f"https://are.na{div_link.get('href')}" for div_link in div_links]

        return img_links
    

    def link_parser(self, link: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(link)  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')

        return html


    def get_img_source(self, html):
        image_src = html.select_one('a[href^="https://d2w9rnfcy7mm78.cloudfront.net/"]').get('href')
        title = html.select_one('img').get('title')
        
        return {'source': image_src, 'title': title}  
    

    def get_img_info(self, link: str, result: None, index: int) -> Image:
            html = self.link_parser(link)
            img_info = self.get_img_source(html)
            image = Image(img_info['title'], link, img_info['source'], 'Are.na', 'None', 'None')

            result[index] = image


    def get_all_img(self, links: list):
        q = queue.Queue()
        for link in links:
            q.put(link)

        num_threads = 10
        threads = [None] * num_threads
        results = [None] * num_threads 
        all_img = list()

        while not q.empty():
            for i in range(num_threads):
                if not q.empty():
                    link = q.get()
                    threads[i] = threading.Thread(target=self.get_img_info, args=(link, results, i), daemon=True)
                    threads[i].start()
            for i in range(num_threads):
                threads[i].join()
            for result in results:
                all_img.append(result)
            
        return all_img
       
            
    
