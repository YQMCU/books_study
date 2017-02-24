# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup

broken_html = '<ul class="country"><li>Area<li>Population</ul>'
# parse the HTML
soup = BeautifulSoup(broken_html,"html.parse")
fixed_html = soup.prettify()
print fixed_html
