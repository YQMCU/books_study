from url_download import download
from bs4 import BeautifulSoup
url = "http://example.webscraping.com/places/view/United-Kingdom-239"
html = download(url)
soup = BeautifulSoup(html,"lxml")
# locate the area row
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'}) # locate the area tag
area = td.text # extract the text from this tag
print area
