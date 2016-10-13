from bs4 import BeautifulSoup
import urllib.request

class Scrapper(object):
    """docstring for Scrapper."""
    def __init__(self, url):
        page = urllib.request.urlopen(url)
        self.raw_data = page.read()

    def print_raw():
        print(self.raw_data)
