#!/usr/bin/env python

# program pro test navstiveni jedne url adresy a stazeni kompletniho obsahu

import sys,time,urllib,lxml,urllib2,re

# url zadana jako prvni parametr
url = sys.argv[1]

start_time = time.time()

page = urllib2.urlopen(url)
page = page.read()

image_links = re.findall(r"<img.*?\s*src=\"(.*?)\".*?", page)
css_links = re.findall(r"<link.*?\s*href=\"(.*?)\".*?", page)
js_links = re.findall(r"<script.*?\s*src=\"(.*?)\".*?", page)

links = []
links.append(image_links)
links.append(css_links)
links.append(js_links)

print image_links
print css_links
print js_links

for url in image_links:
	print "Getting element %s" % (url)
	element = urllib2.urlopen(url)
	element = element.read()

end_time = time.time()

print "Proces trval %.4f" % (end_time - start_time)
