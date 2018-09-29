import re
#import auth
from bs4 import BeautifulSoup
try:
    from .Scrapper import CubaDebate
except (ModuleNotFoundError,ImportError):
    from Scrapper import CubaDebate
import logging
import requests


logger = logging.getLogger('crawler')

dic = {'cubadebate' : CubaDebate}

class Crawler:
    def __init__(self,config={}):
        if isinstance(config,dict):
            if not ("proxy" in config):
                config['proxy'] = {}
            self.__proxy = {
                'http': config["proxy"],
                'https': config["proxy"],
            }
            self.__scrapper = None

        #logger.debug("Created Crawler with config {}".format(config))

    def request(self,url):
        self.__scrapper = None
        for scrapper in dic.values():
            if scrapper.can_crawl(url):
                self.__scrapper = scrapper(url,self.__proxy)
                break
        else:
            raise Exception("Not implemented scrapper")

        #logger.debug("Instanced scraper {}".format(self.__scrapper))

    @property
    def comment(self):
        ans = self.__scrapper.comment
        logger.debug("Extract text {}".format(ans))
        return ans

    @property
    def data(self):
        ans = self.__scrapper.data
        logger.debug("Extract text {}".format(ans))
        return ans
