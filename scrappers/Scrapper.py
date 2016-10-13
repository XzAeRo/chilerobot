from bs4 import BeautifulSoup
import urllib.request
import html2text

class Scrapper(object):
    """docstring for Scrapper."""
    def __init__(self, url):
        self.raw_data = urllib.request.urlopen(url).read()
        self.parsed_data = BeautifulSoup(self.raw_data, 'lxml')

    def print_raw(self):
        print(self.raw_data)

    def get_element(self, css_query):
        return self.parsed_data.select(css_query)

    def to_markdown(self, html_text):
        return html2text.html2text(html_text)
