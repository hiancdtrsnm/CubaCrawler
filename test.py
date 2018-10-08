from Crawler.crawler import Crawler
#from auth import config

#config = {
#    "proxy": "http://user:password@proxy.host:port"
#    }


#c = Crawler(config)
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

c.request('http://www.cubadebate.cu/noticias/2018/10/08/michael-continua-intensificandose-sobre-el-noroeste-del-caribe/#.W7tu8hQpDeM')
text = c.data
comment = c.comment
