# -*- coding : utf-8 -*-

from url_download import download
import re

url = "http://example.webscraping.com/view/United-Kingdom-239"

html = download(url)

re.findall('<td class="w2p_fw"(.*?)</td>',html)