from Crawler.crawler import Crawler
from Crawler import UnreachebleURL
#from auth import config
import logging

logging.basicConfig(level=logging.DEBUG)

#config = {
#    "proxy": "http://user:password@proxy.host:port"
#    }


# c = Crawler(config)
c = Crawler()
#
# c.request("http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/")
# text = c.data
# comment = c.comment
#print(text)
#print(comment)

# c.request("http://www.cubadebate.cu/opinion/2018/09/28/los-comites-de-defensa-de-la-revolucion-estan-en-constante-renovacion/#.W67_VxQpC02")
# text = c.data
# comment = c.comment
#print(text)
#print(comment)

# c.request('http://www.cubadebate.cu/noticias/2017/11/25/comparte-tu-tributo-a-fidel/#.W7tghhQpDeM')
# text = c.data
# comment = c.comment
# print(len(comment))
#print(text)
#print(comment)
try:
    c.request('http://www.cubadebate.cu/noticias/2019/10/14/cuba-avanza-en-la-habilitacion-de-la-tecnologia-4g-lte/#.XaTBdfcpCV4')
    text = c.data
    print(text)
    comment = c.comment
    print(len(comment))
    for i in comment:
        print(i)
except UnreachebleURL as e:
    print(e)
