from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        
        page = context.new_page()
        page.goto(f"https://pinterest.com/search/pins/?q=gojo")  
        page.wait_for_selector("img")  

        html = BeautifulSoup(page.content(), 'html.parser')
        print(html)