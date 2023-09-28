from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    page.goto("https://pinterest.com/search/pins/?q=gojo")  # go to url
    page.wait_for_selector("img")  # wait for content to loadgit 

    soup = BeautifulSoup(page.content(), 'html.parser')
    parsed = []

    for link in soup.findAll('img'):
            print(link.get('src'))
