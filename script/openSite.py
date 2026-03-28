
from playwright.sync_api import sync_playwright

class Site:
    #basic params for opening browser site
    basic_user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/69.0.3497.100 Safari/537.36"
        )
    URL = "https://google.com/"

    #initialization with optional change of params
    def __init__(self,page = URL,user_agent = basic_user_agent,timeout=1000):

            self.URL = page
            self.user_agent = user_agent
            self.timeout = timeout


    def ChangeUserAgent(self,ua):
        self.user_agent = ua

    def ChangeURL(self,url):
        self.URL = url

    #opens site and return content of it
    def GetSite(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(user_agent=self.user_agent)
            page.goto(self.URL)
            page.wait_for_timeout(self.timeout)
            return page.content()
      

