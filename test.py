from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    
    page = context.new_page()
    page.goto(f"https://mn2.mkklcdnv6temp.com/img/tab_28/02/85/28/cc979885/vol3_chapter_44/1-o.jpg")  
    page.wait_for_selector("img")  

    html = BeautifulSoup(page.content(), 'html.parser')

    div_img = html.select_one('img').get('src')

    print(div_img)

    

  