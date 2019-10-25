import re
from urllib3.exceptions import LocationParseError
import logging
import requests


logger = logging.getLogger(__name__)
corchet = re.compile(r'\[[^)]*\]')
parents = re.compile(r'\([^)]*\)')

class UnreachebleURL(Exception):
    pass

class ProxyConfigError(Exception):
    pass

class BadStatusCode(Exception):
    pass

class ScrapBase:
    def __init__(self, url, proxy=None):
        self._comment = None
        self._text = None
        self._url = url
        self._proxy = proxy
        self._html_text = None

    def _request_html(self, url, proxy):
        # logger.debug('_request_html {}, {}'.format(url, proxy))
        try:
            response = requests.get(url, proxies=proxy, timeout=10)
        except Exception as e:
            # logger.debug(e)
            if isinstance(e, LocationParseError):
                try:
                    response = requests.get(url, proxies=proxy['http'], timeout=10)
                except Exception as e:
                    if isinstance(e, LocationParseError):
                        logger.debug(e)
                        raise ProxyConfigError(e.args[0])
                    logger.debug(e)
                    raise UnreachebleURL(e.args[0])
            else:
                logger.debug(e)
                raise UnreachebleURL(e.args[0])
        # logger.debug(response)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            logger.debug("bad response estatus")
            raise BadStatusCode("received code = %d" % response.status_code)
        return response.text

    def Scrap(self, url, proxy=None):
        #logger.debug('_Scrap params {}, {}'.format(url,proxy))
        if self._html_text is None:
            self._html_text = self._request_html(url, proxy)
        #logger.debug(html_text)
        self._text = self._Scrap(url, proxy)

    def Comment(self, url, proxy=None):
        if self._html_text is None:
            self._html_text = self._request_html(url, proxy)
        self._comment = self._Comment(url, proxy)

    def _Scrap(self, url, proxy=None):
        raise NotImplementedError

    def _Comment(self, url, proxy=None):
        raise NotImplementedError

    @property
    def source(self):
        return self._Source()

    def _Source(self):
        raise NotImplementedError


    @property
    def comment(self):
        if self._comment:
            return self._comment

        self.Comment(self._url, self._proxy)

        return self._comment

    @property
    def data(self):
        if self._text:
            return self._text

        self.Scrap(self._url, self._proxy)
        text = self._text['text']
        text = parents.sub('', text)
        text = corchet.sub('', text)
        self._text['text'] = text

        return self._text

    @staticmethod
    def can_crawl(url: str)->bool:
        return False
