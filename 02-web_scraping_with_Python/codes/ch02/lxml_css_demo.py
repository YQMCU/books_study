# -*- coding = utf-8 -*-
from url_download import download
import lxml.html
url = "http://example.webscraping.com/places/view/United-Kingdom-239"
html = download(url)
tree = lxml.html.fromstring(html) # parse the HTML
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print(area)