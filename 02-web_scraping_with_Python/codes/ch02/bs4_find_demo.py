# -*- coding = utf-8 -*-
from bs4 import BeautifulSoup
broken_html = '<ul class="country"><li>Area<li>Population</ul>'
# parse the HTML
soup = BeautifulSoup(broken_html,"html.parse")
ul = soup.find('ul',attrs={'class':'country'})
ul.find('li') # returns just the first match
ur.findall('li') # returns all matches