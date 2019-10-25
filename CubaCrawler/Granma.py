from bs4 import BeautifulSoup
from urllib3.exceptions import LocationParseError
try:
    from .ScrapBase import ScrapBase, UnreachebleURL, ProxyConfigError
except (ModuleNotFoundError,ImportError):
    from ScrapBase import ScrapBase, UnreachebleURL, ProxyConfigError
import requests
import re
import logging
logger = logging.getLogger('scrapper')

from bs4 import BeautifulSoup
try:
    from .ScrapBase import ScrapBase
except (ModuleNotFoundError, ImportError):
    from ScrapBase import ScrapBase
import requests
import re
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

sps = re.compile('  +')
comm = re.compile('comment')


class Granma(ScrapBase):

    def __init__(self,url,proxy=None):
        super().__init__(url,proxy)
        self._html_text = None

    def _Source(self):
        return "Granma"

    def _Scrap(self, url, proxy):
        """
        Search for div with class:note_content and delete footnotes in order to have
        only the desired new text
        """

        soup = BeautifulSoup(self._html_text, 'lxml')
        img = None
        ans = soup.find("article")
        photo = ans.find("div", {"class": "g-story-media-container"})
        if photo:
            img = photo.find('img')
            img = 'http://www.granma.cu'+img['src']
            imgfooter = photo.find("span", {"class": "caption-text"})
            imgfooter = imgfooter.get_text()
        por = ans.find("span", {"class": "byline-author"})
        if por:
            por = por.get_text()
        title = ans.find("h1", {"class": "g-story-heading"}).text
        date = ans.find('time')
        date = datetime.strptime(date.attrs['datetime'], '%Y-%m-%d %H:%M:%S')
        text = ''
        fuente = None
        ans = ans.find("div", {"class": "story-body-textt"})
        for i in ans.find_all('p'):
            txt = i.text.strip()
            text += txt+' '
        ans = text.strip()
        return {'text': ans, 'title': title, 'img': img, 'author': por,
            "pub_date": date, 'img_footer': imgfooter, 'notice_source': fuente}

    def _Comment(self, url, proxy):
        return self._extract_comments(url, proxy)

    def _extract_comments(self, url: str, proxy):
        soup = BeautifulSoup(self._html_text, 'lxml')
        pg = soup.find('ul', {'class': 'pagination'})
        if not pg:
            return self._extract_comments_page(soup)
        comments = []
        comments.extend(self._extract_comments_page(soup))
        for i in pg.find_all('li'):
            if i.attrs.get('class'):
                continue
            url = i.find('a')['href']
            self._html_text = self._request_html(url, proxy)
            soup = BeautifulSoup(self._html_text, 'lxml')
            comments.extend(self._extract_comments_page(soup))
        return comments

    def _extract_comments_page(self, soup):
        """
        Retorna una lista de diccionarios que contienen el texto
        de los comentarios y la fecha en que se hicieron.
        """

        # buscar la seccion de los comentarios
        comments_section = soup.find('div', {"class": 'g-story-comments-list'})
        comments = []
        proc_com = comments_section.find_all(
            'div', attrs={"class": 'media'})
        for i in proc_com:
            data1 = i.find('div',{"class": 'pull-left'})
            data2 = i.find('div',{"class": 'media-body'})
            tt = {}
            tt['author'] = data1.find('p',{'class': 'comment-user'}).contents[0].text
            tt['text'] = data2.find('p',{'class': 'comment-message'}).text.strip()
            date = data1.find('p',{'class': 'comment-date'}).text
            date += data1.find('p',{'class': 'comment-time'}).text
            tt['date'] = self._convert_to_datetime(date)
            comments.append(tt)

        return comments

    def _convert_to_datetime(self, date_string):
        """
        Covierte un string con la estructura 'd m y a las h:m' a datetime
        """
        dict_month = {
            'enero': 'Jan',
            'febrero': 'Feb',
            'marzo': 'Mar',
            'abril': 'Apr',
            'mayo': 'May',
            'junio': 'Jun',
            'julio': 'Jul',
            'agosto': 'Aug',
            'septiembre': 'Sep',
            'octubre': 'Oct',
            'noviembre': 'Nov',
            'diciembre': 'Dec'}

        date = date_string.replace('de ','')
        date = date.split()

        date[1] = dict_month[date[1]]
        string = "".join(date)

        return datetime.strptime(string, '%d%b%Y%H:%M:%S')

    @staticmethod
    def can_crawl(url):
        return 'granma.cu' in url.lower()
