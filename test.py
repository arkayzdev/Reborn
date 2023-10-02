from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    
    page = context.new_page()
    page.goto(f"https://www.pinterest.fr/pin/379639443603815000/")  
    page.wait_for_selector("img")  

    html = BeautifulSoup(page.content(), 'html.parser')

    div_img = html.select('h1')

    print(div_img)

    

  