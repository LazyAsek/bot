

import olxHandler
import os

class Menager:

    #initialize
    def __init__(self,word):
        self.word = word

    #gets links from olx return: set
    def getLinksOlx(self):
        olx = olxHandler.searchOlx(self.word)
        olx.changeSortOrder('new')
        result = olx.search()
        clean_result = olx.clear(result)
        return clean_result

    #saves links in txt separated into newand old ones format: new,count,links old,count,links
    def saveOlx(self,data):
        with open(f"data/olx_links_{self.word}.txt","w") as f:
            for l in data:
                f.write(l+"\n")
            f.close()
    
    def sortNewest(self,data):
        if  not os.path.exists(f"data/olx_links_{self.word}.txt"):
            return data
        new= set()
        old = set()
        with open(f"data/olx_links_{self.word}.txt","r") as f:
            links = set(f.readlines())
            for l in data:
                if l == "new:" or l =="old:":
                    continue
                elif l+"\n" in links:
                    old.add(l)
                else:
                    new.add(l)
        sorted_links=[f"new {len(new)}"]+[i for i in new] +[f"old {len(old)}"]+ [j for j in old]
        return sorted_links
