import olxHandler

olx = olxHandler.searchOlx(word="lego")
olx.changeSortOrder('new')
result = olx.search()
print(result)