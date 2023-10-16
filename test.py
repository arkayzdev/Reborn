from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})

        page = context.new_page()

        page.goto(f"https://www.pinterest.fr/pin/985231162515990/")

        html = BeautifulSoup(page.content(), 'html.parser')
                
        creator_div = html.find('div', attrs={"data-test-id": "official-user-attribution"})
        user_tag = f"@{creator_div.a['href'].replace('/', '')}"
        print(user_tag)
        a