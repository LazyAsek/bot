import linkMenager


lm = linkMenager.Menager("oddam")
olx_links = lm.getLinksOlx()
sorted_olx_links = lm.sortNewest(olx_links)
lm.saveOlx(sorted_olx_links)
