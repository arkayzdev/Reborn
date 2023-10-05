from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class SaveeItService:
    def __init__(self) -> None:
        pass

    def search_parser(self, search: str):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            
            page = context.new_page()
            page.goto(f"https://savee.it/login/")  
            page.wait_for_selector("input")  

            #Login ArkayzScrape:Scrape456951
            username_box = page.locator('input[name="usernameOrEmail"]')
            username_box.type("ArkayzScrape", delay=100)
            
            password_box = page.locator('input[name="password"]')
            password_box.type("Scrape456951", delay=100)
            password_box.press("Enter")
            
