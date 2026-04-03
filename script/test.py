import linkMenager

import olxHandler


"""lm = linkMenager.linkMenager("iphone")
olx_links = lm.getLinksOlx()
sorted_olx_links = lm.sortNewest(olx_links)
lm.saveOlx(sorted_olx_links)
"""

olx = olxHandler.olxHandler("rower")
page = olx.pullTags()
olx.closeOlx()
print(page)