from .Scrapper import Scrapper

class Parser(Scrapper):
    """docstring for Parser."""

    def __init__(self, url):
        super().__init__(url)

    def get_title(self):
        return super().get_element('.datos-noticias h2')[0].get_text()

    def get_subtitle(self):
        return super().get_element('.noticia-single-post figcaption')[0].get_text()

    def get_body(self):
        paragraphs = super().get_element('.txt-post .cuerpo-noticia p')
        body = ''
        for paragraph in paragraphs:
            body += str(paragraph)
        return body

    def parse(self):
        data = '<h1>{}</h1><blockquote>{}</blockquote>{}'.format(self.get_title(), self.get_subtitle(), self.get_body())
        return super().to_markdown(data)
