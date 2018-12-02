class UnreachebleURL(Exception):
    pass

class ProxyConfigError(Exception):
    pass

class ScrapBase:
    def __init__(self,url,proxy=None):
        self.__comment = None
        self.__text = None
        self.__url = url
        self.__proxy = proxy

    def Scrap(self,url,proxy=None):
        self.__text = self._Scrap(url,proxy)

    def Comment(self,url,proxy=None):
        self.__comment = self._Comment(url,proxy)

    def _Scrap(self,url,proxy=None):
        raise NotImplementedError

    def _Comment(self,url,proxy=None):
        raise NotImplementedError

    @property
    def source(self):
        return self._Source()

    def _Source(self):
        raise NotImplementedError


    @property
    def comment(self):
        if self.__comment:
            return self.__comment

        self.__comment = self._Comment(self.__url,self.__proxy)

        return self.__comment

    @property
    def data(self):
        if self.__text:
            return self.__text

        self.__text = self._Scrap(self.__url,self.__proxy)

        return self.__text


    @staticmethod
    def can_crawl(url: str)->bool:
        return False
