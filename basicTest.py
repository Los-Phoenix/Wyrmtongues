import urllib2
from bs4 import BeautifulSoup

response=urllib2.urlopen("https://papers.nips.cc/book/advances-in-neural-information-processing-systems-30-2017")

print response.read()