
import openSite
from bs4 import BeautifulSoup

class olxHandler:

    #setup search in olx with word and optional searach order
    def __init__(self,word,sort = "foru"):
        self.word = "q-"+word
        self.sort = self.__chooseSortOrder(sort)

    #change sort orders from possible orders
    def changeSortOrder(self,new):
        """
        foru, new, cheap, expensive
        if not exsits defoult new descending
        """
        self.sort = self.__chooseSortOrder(new)

    #check if search order exsist (if not go to def) adn return url part needed for search
    def __chooseSortOrder(self,order):
        """
        return; string
        """
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

    
    #open olx site wtih given word ssearched and apropriate search order
    #basic search without tags
    # smaple div syntax search  'div[data-testid="l-card"]'
    def open(self):
        """
        opens browser with given olx url in /oferty
        """
        complete_url ="https://www.olx.pl/oferty/"+self.word+""+self.sort
        print(complete_url)
        self.os = openSite.OpenSite(url=complete_url,timeout=1000,headless=True)
        ret = self.os.GetSite()
        self.page = ret[0]
        self.browser = ret[1]
        
    
    #open website and dynamicly pull tags for word
    #give option to pull all tags
    #lista wszystkich agow laczniez opcjami ich wyboru ( dict )
    #dynamiczne sciagniecie opcji
    def pullTags(self):
        """
        gets all tags 
        without category and price
        esge case for kolor exists

        dict[name] = options
        return ; dict[string] = list[strings]
        """
        #find place with filters
        self.open()
        filters= self.os.parsePage(page=self.page,find='div[data-testid="listing-filters"]')
        
        #get categories andput them to list
        categories = self.os.parsePWObjects(object=filters,find='div[data-testid="multi-select-filter"]')

        #site pulls possible options for given category dynamicly 
        #here we pull name to button that expands options
        name_to_button=[]
        for i in range(0,len(categories)):

            soup_name = self.os.convertToSoup(self.os.convertToHTML(self.os.parsePWObjects(object=categories[i],find='span'))[0])
            name_to_button.append([self.os.getInnerText('span',soup_name)[0] , self.os.parsePWObjects(object=categories[i],find='button')[0]])
 
        #after clicking button pull options and put them to dict
        name_to_options={}
        for i in range(0,len(categories)):
            
            #click each button
            name = name_to_button[i][0]
            name_to_button[i][1].click()

            #get options content
            option_list = self.os.parsePWObjects(object=categories[i],find='div[data-testid="flyout-content"]')[0]
            options_locator = self.os.parsePWObjects(object=option_list,find='p')
            options_html = self.os.convertToHTML(options_locator)

            #extract options from html code
            options=[]
            for o in options_html:
                soup = self.os.convertToSoup(o)
                cur = self.os.getInnerText('p',soup)
                if name== 'Kolor' :
                    if len(cur)>1:
                        options.append(cur[1])
                    else:
                        options.append(cur[0])
                else:
                    options.append(cur[0])

            name_to_options[name] = options
            

        return name_to_options
    
    #get <a> without inner html
    #returns list of unique offers
    def clear(self,olx_html):
        """
        looks through links, get them with from <a> container and put them in proper link format
        return ; set(string)
        """
        elems=[]
        #look through all div[data-testid="l-card"]
        for bit in olx_html:
            soup = self.os.convertToSoup(bit)
            #get all a containers 
            links = soup.find_all('a')
            for l in links:
                #separate link and format it
                unknown = l['href']
                formated_link = unknown if unknown.startswith('http') else f"https://www.olx.pl/{unknown}"
                elems.append(formated_link) 
        return set(elems)

    def closeOlx(self):
        self.os.close(self.browser)
        
 