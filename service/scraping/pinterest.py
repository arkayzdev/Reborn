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
        div_links = html.select('a[href^="/pin/"]') 
        img_links = [f"https://pinterest.com{div_link.get('href')}" for div_link in div_links]
        
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
    

    def get_img_src(self, html) -> tuple:
        """Get the high quality image's link and title

        Args:
            html (_type_): html page parsed with bs4

        Returns:
            tuple: Source/Link , Title
        """
        image_src = html.select_one('img').get('src')

        if "/736x/" in image_src:
            image_src = image_src.replace("/736x/", "/originals/")

        return (image_src, image_src.get('alt'))


    def get_all_img(self, links: list) -> list:
        """Get all links and title of the list

        Args:
            links (list): _description_

        Returns:
            list: List of tuples with (image link, image title)
        """
        all_img = [self.get_img_src(link) for link in links]
        return all_img
    

    def get_title(self, html) -> str:
        """Get image page title defined by Pinterest's user

        Args:
            html (_type_): html page parsed with bs4

        Returns:
            str: title
        """
        title = html.select_one('h1').get_text()
        if title:
            return title
        else:
            return "None"


    def get_user_tag(self, html) -> str:
        """Get image page user tag

        Args:
            html (_type_): html page parsed with bs4

        Returns:
           str: user tag
        """
        creator_div = html.find('div', attrs={"data-test-id": "creator-avatar"})
        return f"@{creator_div.a['href']}"
