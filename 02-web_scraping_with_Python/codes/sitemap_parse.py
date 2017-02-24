# -*- coding = utf-8 -*-

from url_download import download
import re

def crawl_sitemap(url):
	# download the sitemap file
	sitemap = download(url)
	# extract the sitemap links
	links = re.findall('<loc>(.*?)</loc>',sitemap)
	# download each link
	for link in links:
		html = download(link)
		# scrape html here
		# ...
