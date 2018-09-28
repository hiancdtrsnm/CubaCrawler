from Crawler.crawler import Crawler
#from auth import config

config = {
    "proxy": "http://user:password@proxy.host:port"
    }


c = Crawler(config)
#
c.request("http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/")
text = c.text
comment = c.comment
print(text)
print(comment)
#
c.request("http://www.cubadebate.cu/especiales/2018/09/26/la-onu-se-rie-pero-el-problema-con-trump-es-muy-serio/")
text = c.text
comment = c.comment
print(text)
print(comment)

