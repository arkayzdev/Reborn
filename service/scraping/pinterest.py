from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from model.image import Image

class PinterestService:
    def search_parser(self, search: str):
        """Research keywords or theme defined by the user on Pinterest, 
        and parse the html page which contains images related to the input.

        Args:
            search (str): Pinterest research's keywords or theme (pokemon, anime, plane ...)

        Returns:
            _type_: html page parsed with bs4
        """
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(f"https://pinterest.com/search/pins/?q={search}")  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')
            
        return html

    
    def get_links(self, html) -> list:
        """Get images' links from the parsed Pinterest html page

        Args:
            html (_type_): HTML Page

        Returns:
            list: Pinterest images links' list
        """
        links = []
        div_links = html.select('a[href^="/pin/"]') 
        pins = [div_link.get('href') for div_link in div_links]
        for pin in pins:
            if not pin in links:
                links.append(pin)
        img_links = [f"https://pinterest.com{link}" for link in links]
        
        return img_links
    

    def link_parser(self, link: str):
        """Parse the Pinterest image page

        Args:
            link (str): Pinterest image page link

        Returns:
            _type_: html page parsed with bs4
        """
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(link)  
            page.wait_for_selector("img")  

            html = BeautifulSoup(page.content(), 'html.parser')

        return html
    

    def get_img_info(self, html) -> tuple:
        """Get the high quality image's link and title

        Args:
            html (_type_): html page parsed with bs4

        Returns:
            tuple: Source/Link , Title
        """
        image_src = html.select_one('img').get('src')
        alt = html.select_one('img').get('alt')

        if "/736x/" in image_src:
            image_src = image_src.replace("/736x/", "/originals/")

        return {'source': image_src, 'alt': alt}    


    def get_user_tag(self, html) -> str:
        """Get image page user tag

        Args:
            html (_type_): html page parsed with bs4

        Returns:
           str: user tag
        """
        creator_div = html.find('div', attrs={"data-test-id": "official-user-attribution"})
        if creator_div:
            user_tag = f"@{creator_div.a['href'].replace('/', '')}"
        else:
            user_tag = "None"
        return user_tag


    def get_all_img(self, links: list) -> list:
            """Get all informations needed for images

            Args:
                links (list): _description_

            Returns:
                list: List of "Images"
            """
            all_img = []
            for link in links:
                html = self.link_parser(link)
                img_info = self.get_img_info(html)
                author = self.get_user_tag(html)
                all_img.append(Image('None', link, img_info['source'], 'Pinterest', author, img_info['alt']))

            return all_img