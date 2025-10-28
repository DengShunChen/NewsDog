from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = browser.new_page()

    # Wait for the server to start
    time.sleep(10)

    # Go to the home page and take a screenshot
    page.goto("http://localhost:5000")
    page.screenshot(path="jules-scratch/verification/01_home_page.png")

    # Go to the login page and log in
    page.goto("http://localhost:5000/login")
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password')
    page.click('button[type="submit"]')

    # Take a screenshot of the home page after logging in
    page.screenshot(path="jules-scratch/verification/02_home_page_after_login.png")

    # Logout
    page.click('a[href="/logout"]')

    # Take a screenshot of the home page after logging out
    page.screenshot(path="jules-scratch/verification/03_home_page_after_logout.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
