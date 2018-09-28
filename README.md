# CubaCrawler

Esta biblioteca apunta a obtener información de los sitios de
noticias cubanas (Ahora mismo solo funciona [Cubadebate](http://www.cubadebate.cu/)).

## Como se usa

```python
from Crawler import Crawler

data = Crawler()

data.request("http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/#.W6uvSBQpDeM")
print(data.text)
print(data.comment)
```

En caso de tener que pasar por un proxy se puede usar de la siguiente manera

```python
from Crawler import Crawler

config = {
    "proxy": "http://user:password@proxy.host:port"
    }
data = Crawler(config)

data.request("http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/#.W6uvSBQpDeM")
print(data.text)
print(data.comment)
```

O, se pude llamar explicitamente a un Scrapper

```python
from Crawler import Cubadebate

url = "http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/#.W6uvSBQpDeM"
cubadebate = Cubadebate(url)

print(cubadebate.text)
print(cubadebate.comment)
```

Esta biblioteca es desarrollada por GIA (Grupo de Inteligencia Artificial), cualquier contribución o referencia es agradecida.

thanks,

            los autores
