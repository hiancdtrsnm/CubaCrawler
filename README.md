<img alt="PyPI - License" src="https://img.shields.io/pypi/l/CubaCrawler.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/CubaCrawler.svg"> <img alt="PyPI" src="https://img.shields.io/pypi/v/CubaCrawler.svg"> <img alt="Travis (.org)" src="https://img.shields.io/travis/fsadannn/CubaCrawler/master.svg"> <img alt="Codecov" src="https://img.shields.io/codecov/c/github/fsadannn/CubaCrawler.svg">
# CubaCrawler

Esta biblioteca apunta a obtener información de los sitios de
noticias cubanas (Ahora mismo solo funcionan [Cubadebate](http://www.cubadebate.cu/) y
[Granma](http://www.granma.cu/)).

## Como se usa

```python
from CubaCrawler import Crawler

data = Crawler()

data.request("http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/#.W6uvSBQpDeM")
print(data.text)
print(data.comment)
```

En caso de tener que pasar por un proxy se puede usar de la siguiente manera

```python
from CubaCrawler import Crawler

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
from CubaCrawler import Cubadebate

url = "http://www.cubadebate.cu/noticias/2018/09/26/fundada-la-primera-empresa-biotecnologica-cubano-estadounidense-innovative-immunotherapy-alliance-sa/#.W6uvSBQpDeM"
cubadebate = Cubadebate(url)

print(cubadebate.text)
print(cubadebate.comment)
```

Esta biblioteca es desarrollada por GIA (Grupo de Inteligencia Artificial), cualquier contribución o referencia es agradecida.

thanks,

Frank Sadan Naranjo Noda <fsadannn@gmail.com>

Hian Cañizares Díaz <hiancdtrsnm@gmail.com>