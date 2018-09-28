from bs4 import BeautifulSoup
try:
    from .ScrapBase import ScrapBase
except (ModuleNotFoundError,ImportError):
    from ScrapBase import ScrapBase
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

logger = logging.getLogger('scrapper')
logging.basicConfig(level=logging.DEBUG)


class CubaDebate(ScrapBase):

    def _request_html(self, url, proxy):
        #logger.debug('_request_html {}, {}'.format(type(url), type(proxy)))
        try:
            response = requests.get(url, proxies=proxy)
        except Exception as e:
            try:
                response = requests.get(url, proxies=proxy['http'])
            except Exception as e:
                logger.debug(e)
        #logger.debug(response)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            raise Exception("received code = %d" % response.status_code)
        return response.text

    def _Scrap(self, url, proxy):
        """
        Search for div with class:note_content and delete footnotes in order to have
        only the desired new text
        """
        #logger.debug('_Scrap params {}, {}'.format(url,proxy))
        html_text = self._request_html(url, proxy)
        #logger.debug(html_text)

        soup = BeautifulSoup(html_text, 'lxml')
        for item in soup.find_all('div', id=re.compile("^attachment")):
            item.decompose()
        ans = soup.find("div", {"class": "note_content"}).text
        #logger.debug(ans)
        return ans

    def _Comment(self, url, proxy):
        return self._extract_comments(url, proxy)

    def _extract_comments(self, url: str, proxy):
        """
        Retorna una lista de diccionarios que contienen el texto
        de los comentarios y la fecha en que se hicieron.
        """
        html = self._request_html(url, proxy)
        soup = BeautifulSoup(html, 'html.parser')

        # buscar la seccion de los comentarios
        comments_section = soup.find('section', id='comments')
        if comments_section is None:
            return []
        comments_section = comments_section.find('ul')
        if comments_section is None:
            return []

        # obtener el texto de los comentarios
        comments = self._get_comments_info(comments_section)
        # obtener la direccion para mas comentarios
        new_request = comments_section.find(
            'a', attrs={'class': 'pscroll_next'})

        while new_request != None:  # comprobar obtener mas comentarios
            new_url = new_request.get('data-href')
            new_html = self._request_html(new_url, proxy)
            new_soup = BeautifulSoup(new_html, 'html.parser')

            comments += self._get_comments_info(new_soup)
            new_request = new_soup.find('a', attrs={'class': 'pscroll_next'})

        return comments

    def _get_comments_info(self, soup):
        if soup is None:
            return []

        comments_info = []
        # seleccionar todos los tag <li>, clase coments
        comments_list = soup.find_all(
            'li', attrs={'id': re.compile('comment')})
        dict_comments = {}
        for comment in comments_list:
            if comment.ul != None:  # solamente tomar el comentario, no las respuestas a este
                comment.ul.extract()

            # obtener todas las etiquetas <p> del comentario
            tags_p = comment.find_all('p')
            date = comment.find('div', class_='commentmetadata')
            # concatenar el texto de todos los tags <p> del comentario
            dict_comments['text'] = ''.join(tag.get_text() for tag in tags_p)
            dict_comments['date'] = self._convert_to_datetime(date.get_text().strip())

            comments_info.append(dict_comments)

        return comments_info

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

        date = date_string.split()

        date.remove('a')
        date.remove('las')
        date[1] = dict_month[date[1]]
        string = "".join(date)

        return datetime.strptime(string, '%d%b%Y%H:%M')

    @staticmethod
    def can_crawl(url):
        return 'cubadebate' in url.lower()
