# -*- coding : utf-8 -*-

import url_download
import re

def link_crawler(seed_url,link_regex,scrape_callback=None):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    # keep track which URL's have seen before
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            # check if link matches expected regex
        	if re.match(link_regex,link):
                # form absolute link
                link = urlparse.urljoin(seed_url,link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)
        links = []
        if scrape_callback:
            links.extend(scrape_callback(url,html) or [])

def get_links(html):
	"""Return a list of links from html
	"""
	# a regular expression to extract all links from the webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	# list of all links from the webpage
	return webpage_regex.findall(html)

def scrape_callback(url,html):
    if re.search('/view/',url):
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table > tr #places_%s__row > td.w2p_fw' % field)[0].text_content() for field in FIELDS]
        print(url,row)