import re
#import auth
from bs4 import BeautifulSoup
try:
    from .Cubadebate import CubaDebate
    from .Granma import Granma
except (ModuleNotFoundError, ImportError):
    from Cubadebate import CubaDebate
    from Granma import Granma
import logging
import requests


logger = logging.getLogger('crawler')

dic = {'cubadebate': CubaDebate, 'granma': Granma}


class Crawler:
    def __init__(self, config={}):
        if isinstance(config, dict):
            if "proxy" in config:
                self.__proxy = {
                    'http': config["proxy"],
                    'https': config["proxy"],
                }
            elif 'http' in config or 'https' in config:
                self.__proxy = {}
                if 'http' in config and 'https' in config:
                    self.__proxy = {
                        'http': config["http"],
                        'https': config["https"],
                    }
                elif 'http' in config:
                    self.__proxy['http'] = config['http']
                else:
                    self.__proxy['https'] = config['https']
            else:
                self.__proxy = {}
            self.__scrapper = None

        #logger.debug("Created Crawler with config {}".format(config))
    @property
    def source(self):
        if self.__scrapper:
            return self.__scrapper._Source()
        return None

    def request(self, url):
        self.__scrapper = None
        for scrapper in dic.values():
            if scrapper.can_crawl(url):
                self.__scrapper = scrapper(url, self.__proxy)
                break
        else:
            self.__scrapper = scrapper(url, self.__proxy)
            #raise Exception("Not implemented scrapper")

        #logger.debug("Instanced scraper {}".format(self.__scrapper))

    @property
    def comment(self):
        ans = self.__scrapper.comment
        logger.debug("Extract commet {}".format(ans))
        return ans

    @property
    def data(self):
        ans = self.__scrapper.data
        logger.debug("Extract text {}".format(ans))
        return ans
