from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
from pathlib import Path


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    context.add_cookies(json.loads(Path("service/cookies/savee-it.json").read_text()))
    page = context.new_page()
    page.goto(f"https://savee.it/")  
    page.wait_for_selector("img")  

    # #Login ArkayzScrape:Scrape456951
    # username_box = page.locator('input[name="usernameOrEmail"]')
    # username_box.type("ArkayzScrape", delay=100)
    
    # password_box = page.locator('input[name="password"]')
    # password_box.type("Scrape456951", delay=100)
    # password_box.press("Enter")

    # confirm_button = page.locator('button[type="submit"]')
    # confirm_button.click()
    

    

  