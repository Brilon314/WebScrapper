from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:  # En caso de error
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    print(e)
else:
    if html is None:  # En caso que devuelva objeto vacío
        print("URL no encontrada")
    else:
        bsObj = BeautifulSoup(html.read())
try:
    print(bsObj.body.h3)
except AttributeError as e:
    print("No se encontró el tag especificado." + e)
