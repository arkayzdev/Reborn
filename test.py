from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})

        page = context.new_page()

        page.goto(f"https://www.cosmos.so/manifesto")

        html = BeautifulSoup(page.content(), 'html.parser')

        with open('text.txt', 'w', encoding='utf-8') as f:
                f.write(html.get_text())
        
                
