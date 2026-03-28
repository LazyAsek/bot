
import openSite
from bs4 import BeautifulSoup

class searchOlx:

    #setup search in olx with word and optional searach order
    def __init__(self,word,sort = "foru"):
        self.word = word
        self.sort = self.__chooseSortOrder(sort)

    #check if search order exsist (if not go to def) adn return url part needed for search
    def __chooseSortOrder(self,order):
        #possible orders and transletion of them to url fragment responsible for order
        poss = {'foru':"/?search%5Border%5D=relevance:desc",
                'new':"/?search%5Border%5D=created_at:desc",
                'cheap':"/?search%5Border%5D=filter_float_price:asc",
                'expensive':"/?search%5Border%5D=filter_float_price:desc"}
        
        #check if order exists if not set to defoult for you desc
        if order not in poss.keys():
            print ("order not in possible \n possible orders : foru,new,cheap,expensive \n sort order set to basic(for you descending)")
            order_url = "/?search%5Border%5D=relevance:desc"
        else:
            order_url = poss[order]
        return order_url
    
    #change sort orders from possible orders
    def changeSortOrder(self,new):
        self.sort = self.__chooseSortOrder(new)

    #open olx site wtih given word ssearched and apropriate search order
    def search(self):
        complete_url ="https://www.olx.pl/oferty/q-"+self.word+""+self.sort
        print(complete_url)
        olx_page = openSite.Site(page=complete_url,timeout=1000,headless=True)
        olx_code = olx_page.GetSite(find='div[data-testid="l-card"]')
        return olx_code
    
    #get <a> without inner html
    def clear(self,olx_code):

        elems=[]
        #look through all div[data-testid="l-card"]
        for bit in olx_code:
            soup = BeautifulSoup(bit,"html.parser")
            #get all a containers 
            links = soup.find_all('a')
            for l in links:
                #separate link and format it
                unknown = l['href']
                formated_link = unknown if unknown.startswith('http') else f"https://www.olx.pl/{unknown}"
                elems.append(formated_link) 
        return set(elems)

        
 