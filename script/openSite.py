
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class Site:
    #basic params for opening browser site
    with sync_playwright() as p:
            basic_user_agent = p.devices['Desktop Chrome']['user_agent']
    URL = "https://google.com/"

    #initialization with optional change of params
    def __init__(self,page = URL,user_agent = basic_user_agent,timeout=0,headless=False):

            self.URL = page
            self.user_agent = user_agent
            self.timeout = timeout
            self.headless=headless


    def ChangeUserAgent(self,ua):
        self.user_agent = ua

    def ChangeURL(self,url):
        self.URL = url

    #opens site and return content of it
    def GetSite(self,find):
        with sync_playwright() as p:
            #lounch browser
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page(user_agent=self.user_agent)

            #scroll to the bottom and wait to load a page
            page.goto(self.URL)
            page.wait_for_load_state("domcontentloaded")
            page.click("#onetrust-accept-btn-handler")

            previous_count = 0
            for i in range(15): 
                page.keyboard.press("End")
                page.wait_for_timeout(2500) 
                
                current_count = page.locator(find).count()
                
                
                if current_count > previous_count:
                    previous_count = current_count
                else:
                    page.wait_for_timeout(2000)
                    if page.locator(find).count() == previous_count:
                        break

            #get all locator objects
            locator_elements = page.locator(find).all()
            #convert to html
            html_elements=[loc.evaluate("el => el.outerHTML") for loc in locator_elements]
            
            browser.close()
            return html_elements
        
    def checkSite(self,time=10000):
            with sync_playwright() as p:
                #lounch browser
                browser = p.chromium.launch(headless=False)
                page = browser.new_page(user_agent=self.user_agent)

                #scroll to the bottom and wait to load a page
                page.goto(self.URL)
                page.wait_for_timeout(time) 
                browser.close()
    
         
      

