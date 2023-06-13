from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def parse(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_load_state("networkidle")

        html_content = page.content()
        soup = BeautifulSoup(html_content, "html.parser")
        items = soup.find_all('path')

        browser.close()

    return items

