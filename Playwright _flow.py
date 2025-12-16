from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright

def create_app_and_get_code(manifest_url: str, timeout: int = 60) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(manifest_url)

        # GitHub already authenticated via session cookie (GitHub Action runner)
        page.wait_for_selector('button[type="submit"]', timeout=timeout * 1000)
        page.click('button[type="submit"]')

        page.wait_for_url("**?code=*", timeout=timeout * 1000)

        parsed = urlparse(page.url)
        code = parse_qs(parsed.query).get("code", [None])[0]

        browser.close()

        if not code:
            raise RuntimeError("Failed to obtain manifest code")

        return code