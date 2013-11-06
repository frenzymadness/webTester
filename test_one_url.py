#!/usr/bin/env python

# program pro test navstiveni jedne url adresy a stazeni kompletniho obsahu

import sys,time,urllib,lxml,urllib2,re
from thread import start_new_thread

# funkce pro stazeni jednoho souboru
def get_content(url):
	content = urllib2.urlopen(url)
	content = content.read()
	print "Test"

# url zadana jako prvni parametr
url = sys.argv[1]

start_time = time.time()

page = urllib2.urlopen(url)
page = page.read()

image_links = re.findall(r"<img.*?\s*src=\"(.*?)\".*?", page)
css_links = re.findall(r"<link.*?\s*href=\"(.*?)\".*?", page)
js_links = re.findall(r"<script.*?\s*src=\"(.*?)\".*?", page)

links = image_links + css_links + js_links

print links

for url in links:
	start_new_thread(get_content,(url,))

end_time = time.time()

print "Proces trval %.4f" % (end_time - start_time)
