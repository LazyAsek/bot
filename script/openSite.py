
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class OpenSite:
    #basic params for opening browser site
    with sync_playwright() as p:
            basic_user_agent = p.devices['Desktop Chrome']['user_agent']
    URL = "https://google.com/"

    #initialization with optional change of params
    def __init__(self,url = URL,user_agent = basic_user_agent,timeout=0,headless=False):

            self.URL = url
            self.user_agent = user_agent
            self.timeout = timeout
            self.headless=headless


    def ChangeUserAgent(self,ua):
        self.user_agent = ua

    def ChangeURL(self,url):
        self.URL = url

    #opens site and return playwright page of it
    def GetSite(self):
        """
        opens given site in self.url and waits until it fully loads
        return ; page browser
        """
        #lounch browser
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=self.headless)
        page = browser.new_page(user_agent=self.user_agent)

        #scroll to the bottom and wait to load a page
        page.goto(self.URL)
        page.wait_for_load_state("domcontentloaded")
        page.click("#onetrust-accept-btn-handler")
        return [page,browser]

            
    # return page to look
    def checkSite(self,time=100000):
            """
            works like GetSite but do not closes. Used for chekcing site html code and looking through it
            """
            with sync_playwright() as p:
                #lounch browser
                browser = p.chromium.launch(headless=False)
                page = browser.new_page(user_agent=self.user_agent)

                #scroll to the bottom and wait to load a page
                page.goto(self.URL)
                page.wait_for_timeout(time) 
                return [page,browser]
    
    
    def parsePage(self,page,find):
        """
        Looks for given tag/word
        smaple div syntax search  'div[data-testid="l-card"]'
        return type; playwright page object
        """
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
        locator_element = page.locator(find)
        return locator_element
    
    def parsePWObjects(self,object,find):
         """
         return; list[locator Object]
         """
         return object.locator(find).all()
        
    def convertToHTML(self,locator_elements):
        """
        return list[string]
        """
        html_elements=[loc.evaluate("el => el.outerHTML") for loc in locator_elements]
            
        return html_elements
    
    def convertToSoup(self,html_text):
         """
         return soup object
         """
         return BeautifulSoup(html_text,'html.parser')
    
    def getInnerText(self,tag,soup):
        """
        uses bs4 contents, o it returns weird soup string
        return ; list[str (soup type)]
        """
        cur = []
        for container in soup.find(tag).contents:
            cur.append(str(container))
       
        return cur
    
    def close(self,browser):
        browser.close()
         
      

